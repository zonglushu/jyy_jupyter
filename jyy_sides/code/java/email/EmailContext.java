// 上下文类
public class EmailContext {
    private EmailInfo emailInfo;

    public EmailContext(EmailInfo emailInfo) {
        this.emailInfo = emailInfo;
    }

    public void setEmailInfo(EmailInfo emailInfo) {
        this.emailInfo = emailInfo;
    }

    public Email composeEmail() {
        return new Email(emailInfo);
    }
}


