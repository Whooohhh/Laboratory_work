from pathlib import Path
import config
from src.load import load_trips
from src.prepare import prepare_trips
from src.analyze import calculate_metrics
from src.visualize import create_dashboard


def main():
    print('1. Загрузка данных')
    data = load_trips(config.RAW_DIR, config.DATA_PATTERN)

    print('2. Очистка данных')
    clean, quality = prepare_trips(data)
    config.PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    clean.to_csv(config.PROCESSED_DIR / 'trips_clean.csv', index=False)

    print('3. Расчёты')
    metrics = calculate_metrics(clean)
    print('Количество рейсов:', metrics['kpis']['trips'])
    print('Общая выручка:', round(metrics['kpis']['total_revenue']))

    print('4. График и отчёт')
    figure = create_dashboard(clean, metrics, config.FIGURES_DIR / 'dashboard.png')
    report = config.REPORTS_DIR / 'report.md'
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(
        '# Анализ рейсов\n\n'
        f'- Рейсов после очистки: {metrics["kpis"]["trips"]}\n'
        f'- Общая выручка: {metrics["kpis"]["total_revenue"]:,.0f} руб.\n'
        f'- Средняя стоимость рейса: {metrics["kpis"]["mean_trip_cost"]:,.0f} руб.\n'
        f'- Медианная стоимость: {metrics["kpis"]["median_trip_cost"]:,.0f} руб.\n'
        f'- Рейсы без задержки: {metrics["kpis"]["on_time_pct"]:.1f}%\n\n'
        '## Качество данных\n\n'
        f'- До очистки: {quality["строк до обработки"]}\n'
        f'- После очистки: {quality["строк после обработки"]}\n'
        f'- Удалено строк: {quality["удалено строк"]}\n\n'
        '## График\n\n![Dashboard](figures/dashboard.png)\n',
        encoding='utf-8'
    )
    print('Готово. Отчёт:', report)
    print('График:', figure)


if __name__ == '__main__':
    main()
