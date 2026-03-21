#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="${SCRIPT_DIR}/.env"
VENV_ACTIVATE="${SCRIPT_DIR}/.venv/bin/activate"

cd "${SCRIPT_DIR}"

if [ ! -f "${ENV_FILE}" ]; then
  echo "No existe .env en el directorio actual"
  exit 1
fi

set -a
source "${ENV_FILE}"
set +a

if [ -z "${GITHUB_PAT:-}" ]; then
  echo "GITHUB_PAT no está definido tras cargar .env"
  exit 1
fi

if [ ! -f "${VENV_ACTIVATE}" ]; then
  echo "No existe ${VENV_ACTIVATE}"
  exit 1
fi

source "${VENV_ACTIVATE}"

if [ "${1:-}" = "exec" ]; then
  shift
  exec codex exec \
    --sandbox danger-full-access \
    "$@"
fi

exec codex \
  --search \
  --sandbox danger-full-access \
  --ask-for-approval never \
  "$@"
