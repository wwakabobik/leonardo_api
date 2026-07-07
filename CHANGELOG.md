# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.1] - 2023-08-28

### Added
- Leonardo API


## [0.0.2] - 2023-08-29

### Added
- Added CONTRIBUTING, CODE_OF_CONDUCT, SECURITY and pull request templates, also added git workflows/dependabot.


## [0.0.3] - 2023-08-29

### Changed
- README.md


## [0.0.4] - 2023-08-29

### Changed
- README.md


## [0.0.5] - 2023-08-30

### Changed
- Fixed linters warnings
- README.md

## [0.0.6] - 2023-10-14

### Changed
- Updated metadata

## [0.0.7] - 2023-10-15

### Changed
- Updated metadata
- Updated GitHub workflows

## [0.0.8] - 2023-11-22

### Changed
- Fixed wait_for_image_generation method (default is 0 now)
- Updated GitHub workflows (Python 3.12 added for linters)
- Bumped requirements

## [0.0.9] - 2023-11-23

### Fixed
- Fixed headers update methods (possible async bug fix)

## [0.0.10] - 2023-11-24

### Fixed
- Fixed image upload methods (headers should be purged before poking s3)
- Fixed session headers update to much more generic

## [0.0.11] - 2024-11-14

### Fixed
- Fixed linters problems (logging)
- Bumped requirements & badges

## [0.0.12] - 2026-07-07

### Changed
- Dropped Python 3.9 support: pinned dependencies (aiohttp, requests, urllib3) already require Python >=3.10, so `python_requires`/CI matrix now start at 3.10

## [0.0.13] - 2026-07-07

### Fixed
- Fixed Black formatting compliance (missing blank line after module docstring) in `__init__.py`, `src/__init__.py`, `src/__main__.py`, `src/leonardo_api/__init__.py`; this was failing the master `Linters` workflow (pre-existing, unrelated to Python version support)
