// 策略接口
public interface EmailInfo {
    String getContent();
}

// 具体策略类1
public class RegularEmailInfo implements EmailInfo {
    @Override
    public String getContent() {
        return "平常的电子邮件内容。";
    }
}

// 具体策略类2
public class DoubleElevenEmailInfo implements EmailInfo {
    @Override
    public String getContent() {
        return "双十一购物节优惠！";
    }
}

