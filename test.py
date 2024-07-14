# import pandas as pd
# from tkinter import *
# from tkinter import ttk 
# import joblib
# from PIL import Image, ImageTk
# # # Load the dataset
# # df = pd.read_csv(r'C:\Users\huy\HUYYYYYYYY\data_laptop.csv')

# # Load the pre-trained model
# model = joblib.load('best_random_forest_model.joblib')

# # Create Tkinter main
# main = Tk()
# main.title("Used motorbike price prediction")
# #  Lấy ảnh
# path = r'fpt.jpg'
# load = Image.open(path)
# load = load.resize((200, 100))
# render = ImageTk.PhotoImage(load)

# # Đặt vị trí ảnh
# img_label = Label(main, image=render)
# img_label.place(x = 580 , y = 10)
# # Lấy kích thước màn hình
# screen_width = main.winfo_screenwidth()
# screen_height = main.winfo_screenheight()
# # Đặt kích thước và vị trí của cửa sổ
# main.geometry(f'800x400+{screen_width//2-150}+{screen_height//2-100}')
# # Tiêu đề 
# name = Label(main, font = ('Arial', 12), text = 'DANH SÁCH CÁC TÙY CHỌN', bg = 'red', fg = 'white') # tiêu đề
# # Đặt nhãn vào  cửa sổ
# name.place(x = 100, y = 10)
# # dụ đoán giá
# price = Label(main, font = ('Arial', 12), text = 'GIÁ DỰ ĐOÁN', bg = 'red', fg = 'white') # tiêu đề
# # Đặt nhãn vào  cửa sổ
# price.place(x = 450, y = 10)
# # Function to predict price
# def update_combobox(event):
#     global column_1, column_2, column_3, column_4, column_5, column_6, column_7, column_8
#     column_1 = hang.get()
#     column_2 = dong.get()
#     column_3 = namdangki.get()
#     column_4 = soKM.get()
#     column_5 = tinhtrang.get()
#     column_6 = loaixe.get()
#     column_7 = dungtich.get()
#     column_8 = chinhsachBH.get()
# def predict_price():
#     global column_1, column_2, column_3, column_4, column_5, column_6, column_7, column_8
#     # Prepare input data for prediction
#     column_1 = hang.get()
#     column_2 = dong.get()
#     column_3 = namdangki.get()
#     column_4 = soKM.get()
#     column_5 = tinhtrang.get()
#     column_6 = loaixe.get()
#     column_7 = dungtich.get()
#     column_8 = chinhsachBH.get()
#     input_data = {
#         'hang': str(column_1),
#         'dong': str(column_2),
#         'namdangki': column_3,
#         'soKM': column_4,
#         'tinhTrang': str(column_5),
#         'loaiXe': str(column_6),
#         'dungTich': str(column_7),
#         'chinhSachBH': str(column_8)
#     }
#     input_df = pd.DataFrame([input_data])
#     test_predict_price = pipeline.transform(input_df)
#     # Create a DataFrame with the input data
#     try:
#         predicted_price = model.predict(test_predict_price)
#         predicted_price = np.exp(predicted_price)
#         result_label.config(text = f'Predicted Price: {int(predicted_price)}')
#         print(predicted_price)


#     except Exception as e:
#         result_label.config(text=f'Error: {str(e)}')

# # Create and place widgets
# # hãng xe
# hang_label = ttk.Label(main, text="Hãng")
# hang_label.place(x = 50, y = 50)
# hang = ttk.Combobox(main, values = ['Honda', 'Yamaha', 'Piaggio', 
#                                  'SYM', 'Suzuki', 'GPX', 'Ducati', 
#                                  'Kawasaki', 'Brixton', 'Kymco', 
#                                  'Harley Davidson', 'Detech', 'Nioshima', 
#                                  'BMW', 'Benelli', 'Taya', 'Royal Enfield', 
#                                  'Aprilia', 'MV Agusta', 'Peugeot', 
#                                  'Triumph','Daelim', 'Bazan']
#                     , state = 'readonly')
# hang.place(x = 150, y = 50)

# # dòng xe
# dong_label = ttk.Label(main, text="Dòng")
# dong_label.place(x = 50, y = 90)
# dong = ttk.Combobox(main,values = [], state='readonly')
# dong.place(x = 150, y = 90)
# def update_dong(event):
#     check_hang = hang.get()
#     if check_hang == 'Honda':
#         dong['values'] = ['SH', 'Lead', 'Air Blade', 'Vision', 'PCX', 'Winner X', 'Wave', 'SH Mode', 'CB',
#                         'Winner', 'MSX 125', 'Future', 'CD', 'CBR', 'Click', 'Dream', 'Spacy', 'Dylan',
#                         'PS', 'Cub', 'Win', 'Scoopy', 'Rebel', 'Shadow', '67', 'Blade',
#                         'Forza 300', 'Vario', 'Giorno', 'Sonic', 'SCR', 'Beat', 'Chaly']
#     elif check_hang == 'Yamaha':
#         dong['values'] = ['Exciter', 'TFX', 'Nvx', 'R', 'Nouvo', 'MT', 'Grande', 'Janus', 'Cuxi', 'Freego',
#                         'Mio', 'Nozza', 'Sirius', 'Jupiter', 'Latte', 'Acruzo', 'FZ', 'YAZ',
#                         'Taurus']
#     elif check_hang == 'Piaggio':
#         dong['values'] = ['Liberty', 'Zip', 'Vespa', 'Vespa S125', 'Medley', 'Sprint', 'GTS', 'Primavera',
#     'LX', 'Beverly', 'Fly']
#     elif check_hang == 'SYM':
#         dong['values'] = ['Attila', 'Shark', 'Elite', 'Husky', 'Elizabeth', 'Angela', 'Elegant', 'Galaxy']
#     elif check_hang == 'Suzuki':
#         dong['values'] == ['Satria', 'GZ', 'Viva', 'GD', 'Hayate', 'GSX', 'EN', 'Raider', 'Sport / Xipo',
#     'Impulse', 'Sapphire', 'Dòng khác', 'Smash']
#     elif check_hang ==  'GPX':
#         dong['values'] = ['Demon 150GR', 'Legend 200', 'Legend 150S', 'Legend Gentleman 200']
#     elif check_hang == 'Ducati':
#         dong['values'] = ['Monster', '899 panigale', 'Hypermotard']
#     elif check_hang == 'Kawasaki':
#         dong['values'] = ['Kawasaki', 'Z650', 'Dòng khác', 'Z400', 'Z1000', 'Ninja', 'W175', 'Z300', 'Z800',
#     'Vulcan', 'Estrella']
#     elif check_hang == 'Brixton':
#         dong['values'] =  ['BX 150', 'BX 125']
#     else: 
#         dong['values'] = []
# hang.bind('<<ComboboxSelected>>', update_dong)

# # năm đăng kí
# namdangki_label = ttk.Label(main, text="Năm đăng kí")
# namdangki_label.place(x = 50, y = 140)
# namdangki = ttk.Entry(main)
# namdangki.place(x = 150, y = 140)
# namdangki.bind('<<ComboboxSelected>>', update_combobox)

# #số km đã đi
# soKM_label = ttk.Label(main, text="Số KM đã đi")
# soKM_label.place(x = 50, y = 180)
# soKM = ttk.Entry(main)
# soKM.place(x = 150, y = 180)
# soKM.bind('<<ComboboxSelected>>', update_combobox)

# #tình trạng
# tinhtrang_label = Label(main, text="Tình trạng")
# tinhtrang_label.place(x = 50, y = 220)
# tinhtrang = ttk.Combobox(main,values=['Đã sử dụng'], state='readonly')
# tinhtrang.place(x = 150, y = 220)
# tinhtrang.bind('<<ComboboxSelected>>', update_combobox)

# #loại xe
# loaixe_label = ttk.Label(main, text="Loại xe")
# loaixe_label.place(x = 50, y = 260)
# loaixe = ttk.Combobox(main,values = ['Tay côn/Moto', 'Tay ga', 'Xe số'], state='readonly')
# loaixe.place(x = 150, y = 260)
# loaixe.bind('<<ComboboxSelected>>', update_combobox)

# #dung tích xe
# dungtich_label = ttk.Label(main, text="Phân khối")
# dungtich_label.place(x = 50, y = 300)
# dungtich  = ttk.Combobox(main,values=['50 - 100 cc', '100 - 175 cc', 'Trên 175 cc'], state='readonly')
# dungtich.place(x = 150, y = 300)
# dungtich.bind('<<ComboboxSelected>>', update_combobox)

# #chinhSachBH
# chinhsachBH_label = Label(main, text="Bảo hành hãng")
# chinhsachBH_label.place(x = 50, y = 340)
# chinhsachBH = ttk.Combobox(main,values=['Bảo hành hãng', 'Hết bảo hành'], state='readonly')
# chinhsachBH.place(x = 150, y = 340)
# chinhsachBH.bind('<<ComboboxSelected>>', update_combobox)

# def check():

#     if (hang.get() and dong.get() and namdangki.get() and soKM.get() and tinhtrang.get() and loaixe.get() and dungtich.get() and chinhsachBH.get()):
#         predict_price()
#     else:
#         result_label.config(text='Vui lòng nhập đầy đủ dữ liệu')
    
# predict_button = Button(main, text="DỰ ĐOÁN", command=check)
# predict_button.place(x=350, y=340)

# # Add more widgets for other features...

# # predict_button = Button(main, text="DỰ ĐOÁN", command = predict_price)
# # predict_button.place(x = 350, y = 340)

# result_label = Label(main, text="Giá", fg="red", font=("Arial", 15))
# result_label.place(x = 450, y = 200)


# # Run the Tkinter event loop
# main.configure(bg='Orange')
# main.mainloop() 

import tkinter as tk
from tkinter import ttk

def on_select(event):
    selected_year = year_combobox.get()
    print("Năm được chọn là:", selected_year)

root = tk.Tk()
root.title("Chọn năm")

year_combobox = ttk.Combobox(root, state="readonly", width=20)
years = [str(year) for year in range(2000, 2025)]
year_combobox['values'] = years
year_combobox.current(0)  # Thiết lập giá trị mặc định là năm đầu tiên trong danh sách
year_combobox.grid(row=0, column=0, padx=10, pady=10)

year_combobox.bind("<<ComboboxSelected>>", on_select)

root.mainloop()

