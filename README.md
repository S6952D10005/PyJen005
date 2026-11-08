# PyJen005

โปรแกรมบวกเลขอย่างง่ายด้วย Python พร้อม CI/CD ด้วย Jenkins

## การใช้งาน

```bash
python calculator.py 5 7
```

## รันเทสต์

```bash
python -m unittest -v test_calculator.py
```

## Jenkins Pipeline

`Jenkinsfile` มี 3 stage:

1. **Build**: ตรวจ syntax ด้วย `py_compile`
2. **Test**: รัน unit test ด้วย `unittest`
3. **Deploy**: คัดลอกโปรแกรมไปที่ `C:\deploy\PyJen005` แล้วรันโปรแกรม

Jenkins เช็ค GitHub ทุก 1 นาที (Poll SCM) เมื่อมีการ push จะ build, test และ deploy ให้อัตโนมัติ
