#!/usr/bin/env python3
"""验证项目文档 Skill 精确镜像安装和来源清单。"""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INSTALLER_PATH = ROOT / "SoftwareTesting/doc_consistency/install_project_doc_skills.py"

SPEC = importlib.util.spec_from_file_location("project_doc_skill_installer", INSTALLER_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"无法加载安装器: {INSTALLER_PATH}")
INSTALLER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(INSTALLER)


class ProjectDocSkillInstallerTest(unittest.TestCase):
    def test_exact_mirror_and_provenance_verification(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            target = root / "target"
            (source / "project-doc-consistency/references").mkdir(parents=True)
            (source / "project-doc-shared/references").mkdir(parents=True)
            (source / "project-doc-consistency/SKILL.md").write_text(
                "skill\n", encoding="utf-8", newline="\n"
            )
            (source / "project-doc-consistency/references/example.md").write_text(
                "reference\n", encoding="utf-8", newline="\n"
            )
            (source / "project-doc-shared/references/shared.md").write_text(
                "shared\n", encoding="utf-8", newline="\n"
            )
            (target / "project-doc-consistency").mkdir(parents=True)
            (target / "project-doc-consistency/stale.txt").write_text(
                "stale\n", encoding="utf-8"
            )

            metadata = {
                "source_repository": "https://example.invalid/repo.git",
                "source_branch": "main",
                "source_commit": "a" * 40,
            }
            results = INSTALLER.install(
                source,
                target,
                ("project-doc-consistency",),
                metadata,
            )

            self.assertEqual("verified", results[0]["state"])
            self.assertFalse(
                (target / "project-doc-consistency/stale.txt").exists()
            )
            manifest = target / "project-doc-consistency/SOURCE-PROVENANCE.json"
            self.assertTrue(manifest.is_file())

            verified = INSTALLER.verify_manifest(
                target, "project-doc-consistency"
            )
            self.assertEqual("verified", verified["state"], verified)

    def test_modified_installed_file_is_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            target = root / "target"
            (source / "project-doc-consistency").mkdir(parents=True)
            (source / "project-doc-shared/references").mkdir(parents=True)
            (source / "project-doc-consistency/SKILL.md").write_text(
                "skill\n", encoding="utf-8", newline="\n"
            )
            (source / "project-doc-shared/references/shared.md").write_text(
                "shared\n", encoding="utf-8", newline="\n"
            )
            INSTALLER.install(
                source,
                target,
                ("project-doc-consistency",),
                {
                    "source_repository": "repo",
                    "source_branch": "main",
                    "source_commit": "b" * 40,
                },
            )
            (target / "project-doc-shared/references/shared.md").write_text(
                "changed\n", encoding="utf-8", newline="\n"
            )

            result = INSTALLER.verify_manifest(
                target, "project-doc-consistency"
            )
            self.assertEqual("mismatch", result["state"])
            self.assertTrue(
                any("SHA-256 不匹配" in issue for issue in result["issues"]),
                result,
            )

    def test_missing_manifest_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            result = INSTALLER.verify_manifest(
                Path(temporary), "project-doc-consistency"
            )
            self.assertEqual("missing", result["state"])


if __name__ == "__main__":
    unittest.main()
