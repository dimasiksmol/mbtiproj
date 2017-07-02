from django import forms

extraversion = 'extraversion'
introversion = 'introversion'
sensing = 'sensing'
intuition = 'intuition'
thinking = 'thinking'
feeling = 'feeling'
judging = 'judging'
perceiving = 'perceiving'

CHOICE_1 = ((extraversion, 'общаетесь со многими, включая и незнакомцев;'),
            (introversion, 'общаетесь с немногими - Вашими знакомыми.'),)
CHOICE_2 = ((sensing, 'реалистичный, чем склонный теоретизировать;'),
            (intuition, 'склонный теоретизировать, чем реалистичный.'),)
CHOICE_3 = ((sensing, 'витать в облаках;'),
            (intuition, 'придерживаться проторенной дорожки.'),)
CHOICE_4 = ((thinking, 'принципов, законов;'),
            (feeling, 'эмоций, чувств.'),)
CHOICE_5 = ((thinking, 'убеждать;'),
            (feeling, 'затрагивать чувства.'),)
CHOICE_6 = ((judging, 'выполняя все точно в срок;'),
            (perceiving, 'не связывая себя определенными сроками.'),)
CHOICE_7 = ((judging, 'довольно осторожно;'),
            (perceiving, 'внезапно, импульсивно.'),)
CHOICE_8 = ((extraversion, 'остаетесь допоздна, не чувствуя усталости;'),
            (introversion, 'быстро утомляетесь и предпочитаете пораньше уйти.'),)
CHOICE_9 = ((sensing, 'здравомыслящие люди;'),
            (intuition, 'люди с богатым воображением.'),)
CHOICE_10 = ((sensing, 'то, что происходит в действительности;'),
            (intuition, 'те события, которые могут произойти.'),)
CHOICE_11 = ((thinking, 'требования закона, чем обстоятельства;'),
            (feeling, 'обстоятельства, чем требования закона.'),)
CHOICE_12 = ((thinking, 'соблюдать формальности, этикет;'),
            (feeling, 'проявлять свои личные, индивидуальные качества.'),)
CHOICE_13 = ((judging, 'точный, пунктуальный;'),
            (perceiving, 'неторопливый, медлительный.'),)
CHOICE_14 = ((judging, 'оставлять дела незаконченными;'),
            (perceiving, 'непременно доводить дела до конца.'),)
CHOICE_15 = ((extraversion, 'в курсе происходящих событий;'),
            (introversion, 'узнаете о новостях с опозданием.'),)
CHOICE_16 = ((sensing, 'общепринятым способом;'),
            (intuition, 'своим оригинальным способом.'),)
CHOICE_17 = ((sensing, 'выражаются буквально, напрямую;'),
            (intuition, 'пользуются аналогиями, иносказаниями.'),)
CHOICE_18 = ((thinking, 'стройность мысли;'),
            (feeling, 'гармония человеческих отношений'),)
CHOICE_19 = ((thinking, 'в логических умозаключениях;'),
            (feeling, 'в практических оценках ситуаций.'),)
CHOICE_20 = ((judging, 'решены и устроены;'),
            (perceiving, 'не решены и пока не улажены.'),)
CHOICE_21 = ((judging, 'серьезный, определенный;'),
            (perceiving, 'беззаботный, беспечный.'),)
CHOICE_22 = ((extraversion, 'заранее не продумываете все, что нужно сказать;'),
            (introversion, 'мысленно "репетируете" то, что будет сказано.'),)
CHOICE_23 = ((sensing, 'важны сами по себе;'),
            (intuition, 'есть проявления общих закономерностей.'),)
CHOICE_24 = ((sensing, 'раздражают Вас;'),
            (intuition, 'довольно симпатичны Вам.'),)
CHOICE_25 = ((thinking, 'хладнокровный;'),
            (feeling, 'вспыльчивый, горячий.'),)
CHOICE_26 = ((thinking, 'несправедливым;'),
            (feeling, ' беспощадным.'),)
CHOICE_27 = ((judging, 'тщательно взвесив все возможности;'),
            (perceiving, 'полагаясь на волю случая.'),)
CHOICE_28 = ((judging, 'покупать что-нибудь;'),
            (perceiving, 'иметь возможность купить.'),)
CHOICE_29 = ((extraversion, 'первым заводите беседу;'),
            (introversion, 'ждете, когда с Вами заговорят.'),)
CHOICE_30 = ((sensing, 'редко ошибается;'),
            (intuition, 'часто попадает впросак.'),)
CHOICE_31 = ((sensing, 'практичности;'),
            (intuition, 'воображения.'),)
CHOICE_32 = ((thinking, 'тщательно взвесив все возможности;'),
            (feeling, 'полагаясь на волю случая.'),)
CHOICE_33 = ((thinking, 'твердый, чем мягкий;'),
            (feeling, 'мягкий, чем твердый.'),)
CHOICE_34 = ((judging, 'умение методично организовать;'),
            (perceiving, 'умение приспособиться и довольствоваться достигнутым.'),)
CHOICE_35 = ((judging, 'определенность, законченность;'),
            (perceiving, 'открытость, многовариантность.'),)
CHOICE_36 = ((extraversion, 'стимулируют, придают Вам энергии;'),
            (introversion, 'утомляют Вас.'),)
CHOICE_37 = ((sensing, 'человек практического склада;'),
            (intuition, 'человек оригинальный, необычный.'),)
CHOICE_38 = ((sensing, 'находить пользу в отношениях с людьми'),
            (intuition, 'понимать мысли и чувства других.'),)
CHOICE_39 = ((thinking, 'тщательное и всесторонне обсуждение спорного вопроса;'),
            (feeling, 'достижение соглашения по поводу спорного вопроса.'),)
CHOICE_40 = ((thinking, 'рассудком;'),
            (feeling, 'велениями сердца.'),)
CHOICE_41 = ((judging, 'по предварительной договоренности;'),
            (perceiving, 'которая подвернулась случайно.'),)
CHOICE_42 = ((judging, 'на организованность, порядок;'),
            (perceiving, 'на случайность, неожиданность.'),)
CHOICE_43 = ((extraversion, 'много друзей на непродолжительный срок;'),
            (introversion, 'несколько старых друзей.'),)
CHOICE_44 = ((sensing, 'фактами, обстоятельствами;'),
            (intuition, 'общими положениями, принципами.'),)
CHOICE_45 = ((sensing, 'производство и сбыт продукции;'),
            (intuition, 'проектирование и исследования.'),)
CHOICE_46 = ((thinking, 'Вы очень логичный человек;'),
            (feeling, 'Вы тонко чувствующий человек'),)
CHOICE_47 = ((thinking, 'невозмутимость;'),
            (feeling, 'увлеченность.'),)
CHOICE_48 = ((judging, 'окончательные и определенные утверждения;'),
            (perceiving, 'предварительные и неоднозначные утверждения.'),)
CHOICE_49 = ((judging, 'после принятия решения;'),
            (perceiving, 'не ограничивая себя решениями.'),)
CHOICE_50 = ((extraversion, 'легко завязываете продолжительные беседы;'),
            (introversion, 'не всегда находите общие темы для разговора.'),)
CHOICE_51 = ((sensing, 'своему опыту;'),
            (intuition, 'своим предчувствиям.'),)
CHOICE_52 = ((sensing, 'более практичным, чем изобретательным;'),
            (intuition, 'более изобретательным, чем практичным.'),)
CHOICE_53 = ((thinking, 'рассудительный, здравомыслящий человек;'),
            (feeling, 'человек, глубоко переживающий.'),)
CHOICE_54 = ((thinking, 'быть прямым и беспристрастным;'),
            (feeling, 'сочувствовать людям.'),)
CHOICE_55 = ((judging, 'удостовериться, что все подготовлено и улажено;'),
            (perceiving, 'предоставить событиям идти своим чередом.'),)
CHOICE_56 = ((judging, 'на предварительной взаимной договоренности;'),
            (perceiving, 'в зависимости от обстоятельств.'),)
CHOICE_57 = ((extraversion, 'торопитесь подойти первым;'),
            (introversion, 'надеетесь, что подойдет кто-нибудь другой.'),)
CHOICE_58 = ((sensing, 'развитое чувство реальности;'),
            (intuition, 'пылкое воображение.'),)
CHOICE_59 = ((sensing, 'тому, что сказано;'),
            (intuition, 'тому, как сказано.'),)
CHOICE_60 = ((thinking, 'излишняя пылкость, горячность;'),
            (feeling, 'чрезмерная объективность, беспристрастность.'),)
CHOICE_61 = ((thinking, 'трезвым и практичным;'),
            (feeling, 'сердечным и отзывчивым.'),)
CHOICE_62 = ((judging, 'регламентированные и упорядоченные;'),
            (perceiving, 'неупорядоченные и нерегламентированные.'),)
CHOICE_63 = ((judging, 'педантичный, чем капризный;'),
            (perceiving, 'капризный, чем педантичный.'),)
CHOICE_64 = ((extraversion, 'быть открытым, доступным людям;'),
            (introversion, 'быть сдержанным, скрытным.'),)
CHOICE_65 = ((sensing, 'буквальность, конкретность;'),
            (intuition, 'образность, переносный смысл.'),)
CHOICE_66 = ((sensing, 'находить общий язык с другими;'),
            (intuition, 'использовать других в своих интересах.'),)
CHOICE_67 = ((thinking, 'ясности размышлений;'),
            (feeling, 'умения сочувствовать.'),)
CHOICE_68 = ((thinking, 'быть неприхотливым;'),
            (feeling, 'быть излишне привередливым.'),)
CHOICE_69 = ((judging, 'запланированные события;'),
            (perceiving, 'незапланированные события.'),)
CHOICE_70 = ((judging, 'обдуманно, чем импульсивно;'),
            (perceiving, 'импульсивно, чем обдуманно.'),)



class sociotype_test(forms.Form):
    choice_1 = forms.ChoiceField(label = ("1. В компании (на вечеринке) Вы"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_1)
    choice_2 = forms.ChoiceField(label = ("2. Вы человек скорее"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_2)
    choice_3 = forms.ChoiceField(label=("3. По-Вашему, что хуже"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_3)
    choice_4 = forms.ChoiceField(label=("4. Вы более подвержены влиянию"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_4)
    choice_5 = forms.ChoiceField(label=("5.  Вы более склонны"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_5)
    choice_6 = forms.ChoiceField(label=("6. Вы предпочитаете работать"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_6)
    choice_7 = forms.ChoiceField(label=("7. Вы склонны делать выбор"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_7)
    choice_8 = forms.ChoiceField(label=("8. В компании (на вечеринке) Вы"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_8)
    choice_9 = forms.ChoiceField(label=("9. Вас более привлекают"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_9)
    choice_10 = forms.ChoiceField(label=("10. Вам интересно"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_10)
    choice_11 = forms.ChoiceField(label=("11. Оценивая поступки людей, Вы больше учитываете"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_11)
    choice_12 = forms.ChoiceField(label=("12. Обращаясь к другим, Вы скпонны"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_12)
    choice_13 = forms.ChoiceField(label=("13. Вы человек скорее"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_13)
    choice_14 = forms.ChoiceField(label=("14. Вас больше беспокоит необходимость"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_14)
    choice_15 = forms.ChoiceField(label=("15. В кругу знакомых Вы, как правило"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_15)
    choice_16 = forms.ChoiceField(label=("16. Повседневные дела Вам нравится делать"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_16)
    choice_17 = forms.ChoiceField(label=("17. Предпочитаю таких писателей, которые"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_17)
    choice_18 = forms.ChoiceField(label=("18. Что Вас больше привлекает"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_18)
    choice_19 = forms.ChoiceField(label=("19. В чувствуете себя увереннее"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_19)
    choice_20 = forms.ChoiceField(label=("20. Вы предпочитаете, когда дела"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_20)
    choice_21 = forms.ChoiceField(label=("21. Как по-Вашему, Вы человек, скорее"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_21)
    choice_22 = forms.ChoiceField(label=("22. При телефонных разговорах Вы"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_22)
    choice_23 = forms.ChoiceField(label=("23. Как Вы считаете, факты"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_23)
    choice_24 = forms.ChoiceField(label=("24. Фантазеры, мечтатели обычно"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_24)
    choice_25 = forms.ChoiceField(label=("25. Вы чаще действуете как человек"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_25)
    choice_26 = forms.ChoiceField(label=("26. Как по-Вашему, хуже быть"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_26)
    choice_27 = forms.ChoiceField(label=("27. Обычно Вы предпочитаете действовать"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_27)
    choice_28 = forms.ChoiceField(label=("28. Вам приятнее"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_28)
    choice_29 = forms.ChoiceField(label=("29. В компании Вы, как правило"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_29)
    choice_30 = forms.ChoiceField(label=("30. Здравый смысл"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_30)
    choice_31 = forms.ChoiceField(label=("31. Детям часто не хватает"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_31)
    choice_32 = forms.ChoiceField(label=("32. В принятии решений Вы руководствуетесь скорее"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_32)
    choice_33 = forms.ChoiceField(label=("33. Вы человек скорее"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_33)
    choice_34 = forms.ChoiceField(label=("34. Что, по-Вашему, больше впечатляет"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_34)
    choice_35 = forms.ChoiceField(label=("35. Вы больше цените"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_35)
    choice_36 = forms.ChoiceField(label=("36. Новые и нестандартные отношения с людьми"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_36)
    choice_37 = forms.ChoiceField(label=("37. Вы чаще действуете как"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_37)
    choice_38 = forms.ChoiceField(label=("38. Вы более склонны"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_38)
    choice_39 = forms.ChoiceField(label=("39. Что приносит Вам больше удовлетворения"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_39)
    choice_40 = forms.ChoiceField(label=("40. Вы руководствуетесь более"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_40)
    choice_41 = forms.ChoiceField(label=("41. Вам удобнее выполнять работу"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_41)
    choice_42 = forms.ChoiceField(label=("42. Вы обычно полагаетесь"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_42)
    choice_43 = forms.ChoiceField(label=("43 Вы предпочитаете иметь"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_43)
    choice_44 = forms.ChoiceField(label=("44. Вы руководствуетесь в большей степени"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_44)
    choice_45 = forms.ChoiceField(label=("45. Вас больше интересуют"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_45)
    choice_46 = forms.ChoiceField(label=("46. Что Вы считаете за комплимент"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_46)
    choice_47 = forms.ChoiceField(label=("47. Вы более цените в себе"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_47)
    choice_48 = forms.ChoiceField(label=("48. Вы предпочитаете высказывать"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_48)
    choice_49 = forms.ChoiceField(label=("49. Вы лучше чувствуете себя"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_49)
    choice_50 = forms.ChoiceField(label=("50. Общаясь с незнакомыми, Вы"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_50)
    choice_51 = forms.ChoiceField(label=("51. Вы больше доверяете"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_51)
    choice_52 = forms.ChoiceField(label=("52. Вы чувствуете себя человеком"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_52)
    choice_53 = forms.ChoiceField(label=("53. Кто заслуживает большего одобрения"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_53)
    choice_54 = forms.ChoiceField(label=("54. Вы более склонны"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_54)
    choice_55 = forms.ChoiceField(label=("55. Что, по-Вашему, предпочтительней"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_55)
    choice_56 = forms.ChoiceField(label=("56. Отношения между людьми должны строиться"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_56)
    choice_57 = forms.ChoiceField(label=("57. Когда звонит телефон, Вы"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_57)
    choice_58 = forms.ChoiceField(label=("58. Что Вы цените в себе больше"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}), choices=CHOICE_58)
    choice_59 = forms.ChoiceField(label=("59. Вы больше придаете значение"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_59)
    choice_60 = forms.ChoiceField(label=("60. Что выглядит большим заблуждением"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_60)
    choice_61 = forms.ChoiceField(label=("61. Вы в основном считаете себя"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_61)
    choice_62 = forms.ChoiceField(label=("62. Какие ситуации привлекают Вас больше"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_62)
    choice_63 = forms.ChoiceField(label=("63. Вы человек, скорее"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_63)
    choice_64 = forms.ChoiceField(label=("64. Вы чаще склонны"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_64)
    choice_65 = forms.ChoiceField(label=("65. В литературных произведениях Вы предпочитаете"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_65)
    choice_66 = forms.ChoiceField(label=("66. Что для Вас труднее"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_66)
    choice_67 = forms.ChoiceField(label=("67. Чего бы вы себе больше пожелали"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_67)
    choice_68 = forms.ChoiceField(label=("68. Что хуже"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_68)
    choice_69 = forms.ChoiceField(label=("69. Вы предпочитаете"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_69)
    choice_70 = forms.ChoiceField(label=("70. Вы склонны поступать скорее"), widget=forms.RadioSelect(attrs={'class' : 'fieldWrapper_radio'}),
                                  choices=CHOICE_70)