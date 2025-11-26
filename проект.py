import tkinter as tk
import math

def draw_chemistry_diagrams():
    """Отображает схемы BaCl₂ и H₂SO₄ в одном окне Tkinter"""
    root = tk.Tk()
    root.title("Схемы молекул BaCl₂ и H₂SO₄")
    canvas_width = 1200
    canvas_height = 700
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')
    canvas.pack()


    left_center_x = canvas_width // 4
    center_y = canvas_height // 2

    ba_x, ba_y = left_center_x, center_y
    cl_top_x, cl_top_y = left_center_x, center_y - 150
    cl_bottom_x, cl_bottom_y = left_center_x, center_y + 150

    r_ba = 40
    r_cl = 30

    # Ba
    canvas.create_oval(ba_x - r_ba, ba_y - r_ba, ba_x + r_ba, ba_y + r_ba,
                       outline='blue', fill='lightblue', width=2)
    canvas.create_text(ba_x, ba_y, text="Ba", font=("Arial", 16, "bold"), fill="darkblue")

    # Cl сверху
    canvas.create_oval(cl_top_x - r_cl, cl_top_y - r_cl, cl_top_x + r_cl, cl_top_y + r_cl,
                       outline='green', fill='lightgreen', width=2)
    canvas.create_text(cl_top_x, cl_top_y, text="Cl", font=("Arial", 14, "bold"), fill="darkgreen")

    # Cl снизу
    canvas.create_oval(cl_bottom_x - r_cl, cl_bottom_y - r_cl, cl_bottom_x + r_cl, cl_bottom_y + r_cl,
                       outline='green', fill='lightgreen', width=2)
    canvas.create_text(cl_bottom_x, cl_bottom_y, text="Cl", font=("Arial", 14, "bold"), fill="darkgreen")

    def draw_electron_pair(x1, y1, r1, x2, y2, r2):
        dx = x2 - x1
        dy = y2 - y1
        dist = (dx**2 + dy**2)**0.5
        if dist == 0:
            return
        ux, uy = dx / dist, dy / dist
        px1 = x1 + ux * r1
        py1 = y1 + uy * r1
        px2 = x2 - ux * r2
        py2 = y2 - uy * r2
        mx = (px1 + px2) / 2
        my = (py1 + py2) / 2
        perp_x, perp_y = -uy, ux
        offset, rad = 8, 2
        canvas.create_oval(mx + perp_x * offset - rad, my + perp_y * offset - rad,
                           mx + perp_x * offset + rad, my + perp_y * offset + rad,
                           fill='black', outline='black')
        canvas.create_oval(mx - perp_x * offset - rad, my - perp_y * offset - rad,
                           mx - perp_x * offset + rad, my - perp_y * offset + rad,
                           fill='black', outline='black')

    draw_electron_pair(ba_x, ba_y, r_ba, cl_top_x, cl_top_y, r_cl)
    draw_electron_pair(ba_x, ba_y, r_ba, cl_bottom_x, cl_bottom_y, r_cl)


    canvas.create_text(left_center_x, center_y + 200, text="BaCl₂", font=("Arial", 14, "bold"), fill="black")


    right_center_x = 3 * canvas_width // 4
    s_x = right_center_x
    s_y = center_y


    r_s = 35  
    r_o = 25  
    r_h = 18  


    angle_oh1 = math.radians(120)  
    angle_oh2 = math.radians(240)  
    angle_o1 = math.radians(60)    
    angle_o2 = math.radians(300)   


    bond_length_so = 100 
    bond_length_oh = 50   


    o_oh1_x = s_x + bond_length_so * math.cos(angle_oh1)
    o_oh1_y = s_y + bond_length_so * math.sin(angle_oh1)
    h_oh1_x = o_oh1_x - bond_length_oh
    h_oh1_y = o_oh1_y
    
    o_oh2_x = s_x + bond_length_so * math.cos(angle_oh2)
    o_oh2_y = s_y + bond_length_so * math.sin(angle_oh2)
    h_oh2_x = o_oh2_x - bond_length_oh
    h_oh2_y = o_oh2_y


    o1_x = s_x + bond_length_so * math.cos(angle_o1)
    o1_y = s_y + bond_length_so * math.sin(angle_o1)
    o2_x = s_x + bond_length_so * math.cos(angle_o2)
    o2_y = s_y + bond_length_so * math.sin(angle_o2)


    canvas.create_line(s_x, s_y, o_oh1_x, o_oh1_y, width=3, fill='green')
    canvas.create_line(s_x, s_y, o_oh2_x, o_oh2_y, width=3, fill='green')
    

    canvas.create_line(o_oh1_x, o_oh1_y, h_oh1_x, h_oh1_y, width=3, fill='red')
    canvas.create_line(o_oh2_x, o_oh2_y, h_oh2_x, h_oh2_y, width=3, fill='red')


    line_offset = 6  
    canvas.create_line(s_x - line_offset, s_y - line_offset, 
                      o1_x - line_offset, o1_y - line_offset, 
                      width=3, fill='blue')
    canvas.create_line(s_x + line_offset, s_y + line_offset, 
                      o1_x + line_offset, o1_y + line_offset, 
                      width=3, fill='blue')
    canvas.create_line(s_x - line_offset, s_y + line_offset, 
                      o2_x - line_offset, o2_y + line_offset, 
                      width=3, fill='blue')
    canvas.create_line(s_x + line_offset, s_y - line_offset, 
                      o2_x + line_offset, o2_y - line_offset, 
                      width=3, fill='blue')


    canvas.create_oval(s_x - r_s, s_y - r_s, s_x + r_s, s_y + r_s,
                       fill='orange', outline='darkred', width=3)
    canvas.create_text(s_x, s_y, text="S", fill='black', 
                      font=("Arial", 16, "bold"))


    canvas.create_oval(o_oh1_x - r_o, o_oh1_y - r_o, o_oh1_x + r_o, o_oh1_y + r_o,
                       fill='lightgreen', outline='darkgreen', width=2)
    canvas.create_text(o_oh1_x, o_oh1_y, text="O", fill='black', 
                      font=("Arial", 12, "bold"))
    canvas.create_oval(o_oh2_x - r_o, o_oh2_y - r_o, o_oh2_x + r_o, o_oh2_y + r_o,
                       fill='lightgreen', outline='darkgreen', width=2)
    canvas.create_text(o_oh2_x, o_oh2_y, text="O", fill='black', 
                      font=("Arial", 12, "bold"))


    canvas.create_oval(o1_x - r_o, o1_y - r_o, o1_x + r_o, o1_y + r_o,
                       fill='lightblue', outline='darkblue', width=2)
    canvas.create_text(o1_x, o1_y, text="O", fill='black', 
                      font=("Arial", 12, "bold"))
    canvas.create_oval(o2_x - r_o, o2_y - r_o, o2_x + r_o, o2_y + r_o,
                       fill='lightblue', outline='darkblue', width=2)
    canvas.create_text(o2_x, o2_y, text="O", fill='black', 
                      font=("Arial", 12, "bold"))

    canvas.create_oval(h_oh1_x - r_h, h_oh1_y - r_h, h_oh1_x + r_h, h_oh1_y + r_h,
                       fill='pink', outline='red', width=2)
    canvas.create_text(h_oh1_x, h_oh1_y, text="H", fill='black', 
                      font=("Arial", 10, "bold"))
    canvas.create_oval(h_oh2_x - r_h, h_oh2_y - r_h, h_oh2_x + r_h, h_oh2_y + r_h,
                       fill='pink', outline='red', width=2)
    canvas.create_text(h_oh2_x, h_oh2_y, text="H", fill='black', 
                      font=("Arial", 10, "bold"))


    canvas.create_text(right_center_x, center_y + 200, text="H₂SO₄", font=("Arial", 14, "bold"), fill="black")


    plus_x = canvas_width // 2
    plus_y = center_y
    plus_size = 30  

    canvas.create_line(plus_x - plus_size, plus_y, 
                      plus_x + plus_size, plus_y, 
                      width=4, fill='black')

    canvas.create_line(plus_x, plus_y - plus_size, 
                      plus_x, plus_y + plus_size, 
                      width=4, fill='black')

    root.mainloop()

def print_reaction_info1():
    print("=== Химическая реакция: KOH + FeCl₃ ===")
    print("\nРеакция: 3KOH + FeCl₃ → 3KCl + Fe(OH)₃↓\n")
    print("РЕАГЕНТЫ:")
    print("  KOH — прозрачный (бесцветный) раствор")
    print("  FeCl₃ — оранжево-жёлтый раствор\n")
    print("ПРОДУКТ РЕАКЦИИ:")
    print("  Fe(OH)₃ — бурый (ржаво-коричневый) осадок\n")
    print("ФИЗИЧЕСКИЕ СВОЙСТВА Fe(OH)₃:")
    print("  Образует красновато-коричневые кристаллы")
    print("  Нерастворим в воде")
    print("  Плотность: 3,4–3,9 г/см³")
    print("  Температура разложения: ~500 °C\n")
    print("ХИМИЧЕСКИЕ СВОЙСТВА Fe(OH)₃:")
    print("  Реагирует с кислотами с образованием солей железа(III) и воды")
    print("  Окисляется сильными окислителями до ферратов (Fe(VI))")
    print("  При сплавлении со щелочами образует ферриты")
    print("  При нагревании разлагается: 2Fe(OH)₃ → Fe₂O₃ + 3H₂O\n")


def print_reaction_info2():
    print("=== Химическая реакция: BaCl₂ + H₂SO₄ ===")
    print("\nРеакция: BaCl₂ + H₂SO₄ → 2HCl + BaSO₄↓\n")
    print("РЕАГЕНТЫ:")
    print("  BaCl₂ — прозрачный (бесцветный) раствор")
    print("  H₂SO₄ — прозрачный (бесцветный) концентрированный раствор\n")
    print("ПРОДУКТ РЕАКЦИИ:")
    print("  BaSO₄ (сульфат бария) — белый мелкодисперсный осадок\n")
    print("ФИЗИЧЕСКИЕ СВОЙСТВА BaSO₄:")
    print("  Белый кристаллический порошок")
    print("  Нерастворим в воде, кислотах и щелочах")
    print("  Плотность: 4,5 г/см³")
    print("  Температура плавления: ~1580 °C\n")
    print("ХИМИЧЕСКИЕ СВОЙСТВА BaSO₄:")
    print("  Химически инертен при обычных условиях")
    print("  Не реагирует с большинством кислот (включая HCl и HNO₃)")
    print("  Восстанавливается до сульфида бария при сильном нагревании с углём")
    print("  Применяется в медицине (рентгеноконтрастное средство) благодаря своей нерастворимости и низкой токсичности\n")

    while True:
        user_input = input("\nХотите увидеть строение молекул? (да/нет): ").strip().lower()
        if user_input in ('да', 'д', 'yes', 'y'):
            draw_chemistry_diagrams()
            break
        elif user_input in ('нет', 'н', 'no', 'n'):
            print("Хорошо, схемы не будут показаны.")
            break
        else:
            print("Пожалуйста, введите 'да' или 'нет'.")

# Основная программа
print("Введите два реагента (по одному на строку):")
reagent1 = input("Реагент 1: ").strip().upper()
reagent2 = input("Реагент 2: ").strip().upper()

reagents = {reagent1, reagent2}

if {'KOH', 'FECL3'} <= reagents:
    print_reaction_info1()
elif {'BACL2', 'H2SO4'} <= reagents:
    print_reaction_info2()
else:
    print("\n❗ Не обнаружена известная реакция между указанными реагентами.")
    print("Поддерживаемые пары: KOH + FeCl3 или BaCl2 + H2SO4")
