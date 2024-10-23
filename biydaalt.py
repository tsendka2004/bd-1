# Тогтмол утгуудыг тодорхойлно
weeks_per_year = 39  # Хичээлийн жилд 39 долоо хоног гэж үзнэ (9 сарын 1-нээс 6 сарын 1 хүртэл)

# Нийт судалгааны цагийг тооцох функц
def calculate_total_hours(study_years, daily_hours, weekly_days, session_minutes):
    session_hours = session_minutes / 60  # Нэг цагийн үргэлжлэх хугацааг минутаас цагт шилжүүлнэ
    return study_years * weeks_per_year * weekly_days * daily_hours * session_hours

# Сонирхсон хичээлийн цагийг тооцоолох функц
def calculate_interest_hours(study_years, weekly_interest_hours):
    return study_years * weeks_per_year * weekly_interest_hours

# Дадлагын хувь тооцоолох функц
def calculate_internship_percentage(uni_years, internship_weeks):
    total_study_weeks = weeks_per_year * uni_years  # Нийт хичээлийн долоо хоногийн тоо
    return (internship_weeks * uni_years) / total_study_weeks * 100  # Дадлагын эзлэх хувийг олно

# Цаг, өдөр, дадлагын сонголт бүхий меню
def menu():
    while True:
        print("\n== Хичээлийн цаг тооцоолох систем ==")
        print("1. Нийт судалгааны цаг тооцоолох")
        print("2. Сонирхсон хичээлийн цаг тооцоолох")
        print("3. Дадлагын хувийг тооцоолох")
        print("4. Гарах")
        
        choice = input("Сонголтоо хийнэ үү (1-4): ")

        if choice == '1':
            study_years = int(input("Судалсан жил: "))
            daily_hours = float(input("Өдөрт хичээллэх цаг: "))
            weekly_days = int(input("7 хоногт хичээллэх өдөр: "))
            session_minutes = int(input("Нэг цагийн үргэлжлэх хугацаа (минутаар): "))
            total_hours = calculate_total_hours(study_years, daily_hours, weekly_days, session_minutes)
            print(f"\nНийт судалсан цаг: {total_hours:.2f} цаг\n")

        elif choice == '2':
            study_years = int(input("Судалсан жил: "))
            weekly_interest_hours = float(input("7 хоногт сонирхсон хичээлд зарцуулсан цаг: "))
            interest_hours = calculate_interest_hours(study_years, weekly_interest_hours)
            print(f"\nНийт сонирхсон хичээлд зарцуулсан цаг: {interest_hours:.2f} цаг\n")

        elif choice == '3':
            uni_years = int(input("Их сургуулийн жил: "))
            internship_weeks = int(input("Дадлагын долоо хоног: "))
            internship_percentage = calculate_internship_percentage(uni_years, internship_weeks)
            print(f"\nДадлагын эзлэх хувь: {internship_percentage:.2f}%\n")

        elif choice == '4':
            print("Программыг хаалаа.")
            break

        else:
            print("Буруу сонголт. Дахин оролдоно уу.")

# Программыг ажиллуулна
menu()
