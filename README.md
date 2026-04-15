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
