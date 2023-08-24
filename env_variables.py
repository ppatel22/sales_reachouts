import pandas as pd

sample_df = pd.DataFrame(
    {
        "companies": ["PKT Ventures"],
        "emails": ["princepatel1304@outlook.com"],
        "Fund type": ["Venture Fund"],
        "firstname": ["Prince"],
    }
)


no_no_list = [
    "Sequoia Capital",
    "Andreessen Horowitz",
    "a16z",
    "Kleiner Perkins",
    "Point72 Ventures",
    "Cory Levy",
    "Forefront Venture Partners",
    "Samsung NEXT" "Angeleno Group",
    "Caravel Investment Group",
    "Inertia Ventures",
    "Holt Ventures",
    "East Ventures",
    "UP.Partners",
    "Render Capital",
    "Baukunst",
    "Nocap Ventures",
    "The Caravel Group",
    "Sozo Ventures",
    "Susa Ventures",
    "Sequoia",
    "XFund",
    "Long Journey Ventures",
    "Insight Partners",
    "Forerunner",
    "Quiet Capital",
    "Gobi Ventures",
    "SALT Fund",
    "Glasswing",
    "Xontogeny",
    "SNØCAP",
    "Connecticut Innovations",
    "Decent Capital",
    "Red Sea Ventures",
    "Remus",
    "Innospark",
]
reached_path = "companies_reached.csv"
reached_df = pd.read_csv(reached_path)
