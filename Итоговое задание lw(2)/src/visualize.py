from pathlib import Path
import matplotlib.pyplot as plt


def create_dashboard(df, metrics, save_path):
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    monthly = metrics['monthly']
    axes[0, 0].plot(monthly['month'], monthly['revenue_mln'], marker='o')
    axes[0, 0].set_title('Выручка по месяцам')
    axes[0, 0].set_ylabel('млн руб.')

    route = metrics['route_stats']['revenue'] / 1_000_000
    axes[0, 1].barh(route.index, route.values)
    axes[0, 1].set_title('Выручка по маршрутам')
    axes[0, 1].set_xlabel('млн руб.')

    axes[1, 0].hist(df['cost_rub'], bins=25)
    axes[1, 0].set_title('Стоимость рейсов')
    axes[1, 0].set_xlabel('руб.')

    carriers = metrics['carrier_stats']['OTD_pct'].sort_values()
    axes[1, 1].barh(carriers.index, carriers.values)
    axes[1, 1].set_title('OTD перевозчиков')
    axes[1, 1].set_xlabel('% рейсов без задержки')

    fig.tight_layout()
    path = Path(save_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=140)
    plt.close(fig)
    return path
