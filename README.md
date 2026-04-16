# DevOps Demo API

FastAPI 기반 DevOps 파이프라인 데모 프로젝트입니다.

## 로컬 개발

### 의존성 설치

```bash
uv sync
```

### 서버 실행

```bash
uv run uvicorn main:app --reload
```

서버 실행 후 http://localhost:8000/docs 에서 Swagger UI 확인 가능

### 테스트 실행

```bash
uv run pytest
```

## Docker 빌드

### 이미지 빌드

```bash
docker build -t devops-demo-api .
```

### 컨테이너 실행

```bash
docker run -p 8000:8000 devops-demo-api
```

## CI/CD 파이프라인

| 워크플로우 | 트리거 | 동작 |
|---|---|---|
| CI (`ci.yml`) | PR, `main`/`develop` push | 테스트 → Docker 빌드 |
| CD (`cd.yml`) | `main` push, `v*.*.*` 태그 | GHCR 이미지 push → 배포 |

### 릴리즈 배포

```bash
git tag v1.0.0
git push origin v1.0.0
```

태그 push 시 CD 파이프라인이 자동으로 실행됩니다.

# Git Commit Signing
```bash
# 1) GitHub CLI 다시 로그인
gh auth login -h github.com

# 2) 현재 SSH 공개키를 GitHub에 "signing key"로 등록
# 같은 키를 auth 용도로 이미 올렸어도 signing 용도로 한 번 더 추가해야 함
gh ssh-key add ~/.ssh/id_ed25519.pub --type signing --title "woojin-mac-signing"

# 3) Git에 서명 설정
git config --local gpg.format ssh
git config --local user.signingkey ~/.ssh/id_ed25519.pub
git config --local commit.gpgsign true

# 선택
git config --local tag.gpgSign true
```