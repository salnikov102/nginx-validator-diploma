#!/usr/bin/env python3
"""
Скрипт автоматизированной behavioral-валидации конфигураций Nginx.
Ядро проекта
"""
import subprocess
import sys

def run_command(command, description):
    """Запускает команду и выводит результат."""
    print(f"\n {description}...")
    print(f"   Команда: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.stdout:
        for line in result.stdout.strip().split("\n"):
            print(f"{line}")
    if result.returncode != 0:
        print(f"{result.stderr.strip()}")
        
    return result.returncode == 0

def main():
    print("="*50)
    print("АВТОМАТИЗИРОВАННАЯ ВАЛИДАЦИЯ КОНФИГУРАЦИИ NGINX")
    print("="*50)

    # 1. Проверка синтаксиса (стандартный этап)
    if not run_command("docker compose exec -T nginx nginx -t", "Проверка синтаксиса nginx -t"):
        print("\n ВАЛИДАЦИЯ ЗАВЕРШЕНА: синтаксические ошибки в конфигурации.")
        sys.exit(1)
    print(" Синтаксис корректен.")

    # 2. Запуск поведенческих тестов
    if not run_command("python -m pytest tests/test_scenarios.py -v", "Запуск behavioral-тестов"):
        print("\n ВАЛИДАЦИЯ ЗАВЕРШЕНА: тесты runtime-поведения не пройдены.")
        sys.exit(1)
    print(" Поведенческие сценарии отработали успешно.")

    print("\n" + "="*50)
    print(" ВАЛИДАЦИЯ УСПЕШНА! Конфигурация безопасна для деплоя.")
    print("="*50)

if __name__ == "__main__":
    main()