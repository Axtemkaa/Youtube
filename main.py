menu_label = """
|-----------------------------------------------------------------------------------|
| ███   ███    ███████    ███   ███   █████████   ███   ███   ████████    █████████ |
|  ███ ███    ███   ███   ███   ███      ███      ███   ███   ███   ███   ███       |
|   █████     ███   ███   ███   ███      ███      ███   ███   ████████    ███       |
|    ███      ███   ███   ███   ███      ███      ███   ███   ███   ███   █████████ |
|    ███      ███   ███   ███   ███      ███      ███   ███   ███   ███   ███       |
|    ███       ███████     ███████       ███       ███████    ████████    █████████ |
|-----------------------------------------------------------------------------------|
Наслаждайтесь просмотром :)
С душой от Azxctem
-------------------
|1| Начать допрос |
|2| Выйти         |
-------------------
"""

themes = [
    "Реакции на видео", "Челленджи", "Обзор мемов", "Скетчи", "Пранки", 
    "Влоги", "Обзор игр", "Стримы", "Shorts", "Туториалы", "Распаковки",
    "Эксперименты", "Лайфхаки", "Обзор Reddit", "Тик-Ток реакции", "Minecraft",
    "Roblox", "Among Us", "Реакции на клипы", "Обзор комментариев", "Обзоры техники",
    "DIY проекты", "Готовка", "Путешествия", "Спорт", "Музыкальные каверы",
    "Анимация", "Образование", "Наука", "Технологии", "Мода", "Красота",
    "Здоровье", "Фитнес", "Юмор", "Интервью", "Документальные", "Новости",
    "Обзор фильмов", "Обзор сериалов"
]

questions = {
    "ask1": "Короткое/длинное видео?",
    "ask2": "Тема видео (0 для готовых тем)?",
    "ask3": "Основная тематика?",
    "ask4": "Развлекательное/Информативное?", 
    "ask5": "Туториал/Обучение?",
    "ask6": "Возрастное ограничение?",
    "ask7": "Наличие спецэффектов?",
    "ask8": "Музыкальное сопровождение?",
    "ask9": "Наличие диалогов?",
    "ask10": "Съемка от первого/третьего лица?",
    "ask11": "Качество видео (HD/4K)?",
    "ask12": "Наличие субтитров?",
    "ask13": "Язык видео?",
    "ask14": "Год выпуска?",
    "ask15": "Популярность канала?",
    "ask16": "Продолжительность (в минутах)?",
    "ask17": "Жанр видео?",
    "ask18": "Целевая аудитория?",
    "ask19": "Наличие рекламы?",
    "ask20": "Формат видео (блог/шоу/влог)?",
    "ask21": "Название канала (оставьте пустым, если не важно)?"
}

def get_video_type(answer):
    answer = answer.lower()
    if answer in ['короткое', 'short', 'shorts']:
        return 'shorts'
    elif answer in ['длинное', 'long']:
        return 'video'
    return None

def get_theme_from_list(user_input):
    if user_input == '0':
        print("\nДоступные темы:")
        for i, theme in enumerate(themes, 1):
            print(f"{i}. {theme}")
        while True:
            try:
                choice = input("\nВыберите номер темы (1-40): ")
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(themes):
                    return themes[choice_idx]
                print("Пожалуйста, выберите число от 1 до 40")
            except ValueError:
                print("Пожалуйста, введите корректное число")
    return user_input

def process_question(question, is_theme_question=False):
    answer = input(f"{question} ").strip()
    return get_theme_from_list(answer) if is_theme_question else answer

def start_interrogation():
    video_type = get_video_type(process_question(questions["ask1"]))
    selected_theme = process_question(questions["ask2"], is_theme_question=True)
    main_topic = process_question(questions["ask3"], is_theme_question=True)
    
    answers = {
        "Тип видео": "YouTube Shorts" if video_type == "shorts" else "Обычное видео",
        "Тема": selected_theme,
        "Основная тематика": main_topic
    }
    
    # Добавляем остальные ответы
    for key, question in list(questions.items())[3:]:
        answers[question.rstrip("?")] = process_question(question)
    
    print("\nРезультаты опроса:")
    print("-" * 50)
    for key, value in answers.items():
        print(f"{key}: {value}")
    print("-" * 50)
    
    # Формируем поисковый запрос
    search_terms = [
        selected_theme,
        main_topic,
        answers.get("Жанр видео", ""),
        answers.get("Основная тематика", "")
    ]
    search_query = " ".join(term for term in search_terms if term)
    
    # Формируем поисковый URL с корректным кодированием
    from urllib.parse import quote
    base_url = "https://www.youtube.com/"
    encoded_query = quote(search_query)
    search_url = f"{base_url}{'shorts/search?q=' if video_type == 'shorts' else 'results?search_query='}{encoded_query}"
    
    print(f"\nСсылка для поиска: {search_url}")
    
    choice = input("\nНажмите Enter для продолжения или 'q' для выхода: ")
    if choice.lower() == 'q':
        return False
    return True

def main():
    while True:
        print(menu_label)
        choice = input("Выберите опцию: ")
        
        if choice == "1":
            if not start_interrogation():
                break
        elif choice == "2":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1 или 2.")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
