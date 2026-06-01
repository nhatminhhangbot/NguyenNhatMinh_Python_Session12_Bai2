"""
- Dữ liệu đầu vào: Một danh sách saving_accounts chứa các dictionary.
Mỗi dictionary đại diện cho một sổ tiết kiệm với các key: account_id (str), customer_name (str), balance (int), term_months (int), interest_rate (float), status (str).
- Menu chức năng:
    + Input: Lựa chọn menu (Chuỗi/Số nguyên từ 1-7)
    + Output: Hiển thị chức năng hoặc thông báo lỗi nếu nhập sai
- Chức năng 1:
    + Input: Không có
    + Output: Danh sách thông tin các sổ tiết kiệm hoặc thông báo danh sách trống
- Chức năng 2:
    + Input: Mã sổ tiết kiệm (str), Tên khách hàng (str), Số tiền gửi (int), Kỳ hạn theo tháng (int), Lãi suất năm (float)
    + Output: Thêm thành công sổ tiết kiệm mới vào list hoặc báo lỗi (trùng mã, trống tên, sai số...)
- Chức năng 3:
    + Input: Mã sổ tiết kiệm cần sửa và các thông tin mới tương tự chức năng 2
    + Output: Cập nhật thành công giá trị trong sổ tương ứng hoặc báo lỗi (không tồn tại, đã closed, sai định dạng)
- Chức năng 4:
    + Input: Mã sổ tiết kiệm (str)
    + Output: Chuyển status từ "active" sang "closed" hoặc báo lỗi
- Chức năng 5:
    + Input: Mã sổ tiết kiệm (str)
    + Output: Tiền lãi dự kiến (Float), Tổng tiền nhận (Float) hoặc báo lỗi
- Chức năng 6:
    + Input: Mã sổ tiết kiệm (str), Số tháng thực gửi (int)
    + Output: Tiền lãi thực nhận, Tổng tiền thực nhận (áp dụng lãi suất phù hợp) hoặc báo lỗi
"""

saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán hoặc xóa sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")
    choice = input("Nhập lựa chọn của bạn (1-7): ").strip()

    if choice == "1":
        if len(saving_accounts) == 0:
            print("Danh sách sổ tiết kiệm hiện đang trống.")
        else:
            print("Danh sách sổ tiết kiệm:")
            for index, account in enumerate(saving_accounts, start = 1):
                print(f"{index}. Mã sổ: {account["account_id"]} | "
                      f"Khách hàng: {account['customer_name']} | "
                      f"Số tiền gửi: {account['balance']} | "
                      f"Kỳ hạn: {account['term_months']} tháng | "
                      f"Lại suất: {account['interest_rate']}%/năm | "
                      f"Trạng thái: {account['status']}")
    elif choice == "2":
        account_id = input("Nhập mã sổ tiết kiệm: ").strip().upper()

        is_duplicate = False
        for account in saving_accounts:
            if account["account_id"] == account_id:
                is_duplicate = True
                break

        if is_duplicate:
            print("Mã sổ tiết kiệm đã tồn tại!")
            continue

        customer_name = input("Nhập tên khách hàng: ").strip()
        if customer_name == "":
            print("Tên khách hàng không được để trống.")
            continue

        balance_input = input("Nhập số tiền gửi: ").strip()
        if balance_input == "" or not balance_input.isdigit():
            print("Số tiền gửi không hợp lệ!")
            continue
        balance = int(balance_input)
        if balance <= 0:
            print("Số tiền gửi không hợp lệ!")
            continue

        term_input = input("Nhập kỳ hạn gửi theo tháng: ").strip()
        if term_input == "" or not term_input.isdigit():
            print("Kỳ hạn không hợp lệ!")
            continue
        term_months = int(term_input)
        if term_months <= 0:
            print("Kỳ hạn không hợp lệ!")
            continue

        rate_input = input("Nhập lãi suất năm: ").strip()
        if rate_input == "" or not rate_input.replace(".", "", 1).isdigit():
            print("Lãi suất không hợp lệ!")
            continue
        interest_rate = float(rate_input)
        if interest_rate <= 0:
            print("Lãi suất không hợp lệ!")
            continue

        new_account = {
            "account_id": account_id,
            "customer_name": customer_name,
            "balance": balance,
            "term_months": term_months,
            "interest_rate": interest_rate,
            "status": "active"
        }
        saving_accounts.append(new_account)
        print("Mở sổ tiết kiệm mới thành công.")
    elif choice == "3":
        account_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ").strip().upper()
        find = None
        for account in saving_accounts:
            if account["account_id"] == account_id:
                find = account
                break

        if find is None:
            print("Không tìm thấy mã sổ tiết kiệm.")
            continue

        if find["status"] == "closed":
            print("Không thể thao tác với sổ tiết kiệm đã tất toán.")
            continue

        new_name = input("Nhập tên khách hàng mới: ").strip()
        if new_name == "":
            print("Tên khách hàng không được để trống.")
            continue

        new_balance_input = input("Nhập số tiền gửi: ").strip()
        if new_balance_input == "" or not new_balance_input.isdigit():
            print("Số tiền gửi không hợp lệ!")
            continue
        new_balance = int(new_balance_input)
        if new_balance <= 0:
            print("Số tiền gửi không hợp lệ!")
            continue

        new_term_input = input("Nhập kỳ hạn gửi theo tháng: ").strip()
        if new_term_input == "" or not new_term_input.isdigit():
            print("Kỳ hạn không hợp lệ!")
            continue
        new_term_months = int(new_term_input)
        if new_term_months <= 0:
            print("Kỳ hạn không hợp lệ!")
            continue

        new_rate_input = input("Nhập lãi suất năm: ").strip()
        if new_rate_input == "" or not new_rate_input.replace(".", "", 1).isdigit():
            print("Lãi suất không hợp lệ!")
            continue
        new_interest_rate = float(new_rate_input)
        if new_interest_rate <= 0:
            print("Lãi suất không hợp lệ!")
            continue

        find["customer_name"] = new_name
        find["balance"] = new_balance
        find["term_months"] = new_term_months
        find["interest_rate"] = new_interest_rate
        print("Cập nhật thông tin sổ tiết kiệm thành công.")
    elif choice == "4":
        account_id = input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ").strip().upper()
        find = None
        for account in saving_accounts:
            if account["account_id"] == account_id:
                find = account
                break

        if find is None:
            print("Không tìm thấy mã sổ tiết kiệm.")
            continue

        if find["status"] == "closed":
            print("Sổ tiết kiệm này đã được tất toán trước đó rồi.")
            continue

        find["status"] = "closed"
        print(f"Tất toán sổ tiết kiệm {account_id} thành công.")
    elif choice == "5":
        account_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ").strip().upper()
        find = None
        for account in saving_accounts:
            if account["account_id"] == account_id:
                find = account
                break

        if find is None:
            print("Không tìm thấy mã sổ tiết kiệm.")
            continue

        if find["status"] == "closed":
            print("Không thể thao tác với sổ tiết kiệm đã tất toán.")
            continue

        balance = find["balance"]
        interest_rate = find["interest_rate"]
        term_months = find["term_months"]

        interest = balance * (interest_rate / 100) * (term_months / 12)
        total_received = balance + interest

        print(f"Tiền lãi dự kiến: {interest:.2f} VND")
        print(f"Tổng tiền nhận khi đến hạn: {total_received:.2f} VND")
    elif choice == "6":
        account_id = input("Nhập mã sổ tiết kiệm cần kiểm tra: ").strip().upper()
        find = None
        for account in saving_accounts:
            if account["account_id"] == account_id:
                find = account
                break

        if find is None:
            print("Không tìm thấy mã sổ tiết kiệm.")
            continue

        if find["status"] == "closed":
            print("Không thể thao tác với sổ tiết kiệm đã tất toán.")
            continue

        real_months_input = input("Nhập số tháng thực gửi: ").strip()
        if real_months_input == "" or not real_months_input.isdigit():
            print("Số tháng thực gửi không hợp lệ!")
            continue
        real_months = int(real_months_input)
        if real_months <= 0:
            print("Số tháng thực gửi không hợp lệ!")
            continue

        balance = find["balance"]
        original_term = find["term_months"]

        if real_months < original_term:
            print("Thông báo: Khách hàng rút trước hạn. Áp dụng lãi suất không kỳ hạn (0.5%/năm).")
            applied_rate = 0.5
        else:
            print("Thông báo: Khách hàng đủ điều kiện hưởng lãi đúng hạn.")
            applied_rate = find["interest_rate"]

        interest_received = balance * (applied_rate / 100) * (real_months / 12)
        total_received = balance + interest_received

        print(f"Lãi suất áp dụng: {applied_rate}%/năm")
        print(f"Tiền lãi thực nhận: {interest_received:.2f} VND")
        print(f"Tổng tiền thực nhận: {total_received:.2f} VND")
    elif choice == "7":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 7.")