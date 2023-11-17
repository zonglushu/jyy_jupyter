public class Email {
    private EmailInfo emailInfo;

    public Email(EmailInfo emailInfo) {
        this.emailInfo = emailInfo;
    }

    public String getContent() {
        return emailInfo.getContent();
    }
}
