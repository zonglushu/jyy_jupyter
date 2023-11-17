public class EmailSenderProxy {
    // 委托给策略对象的方法
    public void sendEmail(Email email) {
        String content = email.getContent(); // 获取策略提供的内容
        System.out.println("发送邮件: " + content);
        // 在实际应用中，这里可以添加发送电子邮件的逻辑
    }
}