from ..src.athlete import Athlete
# from ..src.vo2_max_data import vo2_max_data
from ..src.examples import examples


def test_get_bmi():
    name = "kobe_bryant"

    kobe = Athlete(
        name=name,
        gender=examples[name].get("gender", "Gender not specified"),
        dob=examples[name].get("dob", "Date of birth is missing!"),
        height=examples[name].get("height", "Height is missing!"),
        bodyweight=examples[name].get("bodyweight", "Bodyweight is missing!"),
        hr_rest=examples[name].get("hr_rest", ""),
        sport=examples[name].get("sport", ""),
        death_date=examples[name].get("death_date", ""),
    )

    assert kobe.get_bmi() == 0.00245
