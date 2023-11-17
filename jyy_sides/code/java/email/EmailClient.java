public class EmailClient {
    public static void main(String[] args) {
        EmailContext emailContext = new EmailContext(new RegularEmailInfo());
        EmailSenderProxy emailSender = new EmailSenderProxy();
        
        // 发送平常的邮件
        Email email=emailContext.composeEmail();
        emailSender.sendEmail(email);

        // 切换到双十一活动邮件
        emailContext.setEmailInfo(new DoubleElevenEmailInfo());
        Email email1=emailContext.composeEmail();
        emailSender.sendEmail(email1);

        // 对于不同的活动，可以继续切换邮件信息策略并发送
    }
}
