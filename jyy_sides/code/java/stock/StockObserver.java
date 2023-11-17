package code.java.stock;

// 股票观察者类
class StockObserver {
    private static Topic topic;

    public static void setTopic(Topic topic) {
        StockObserver.topic = topic;
    }

    // 股票观察者监听到topic的变化后，将这个信息传给toic
    public static void notify(String stockSymbol, String message) {
        if (topic != null) {
            topic.receiveUpdate(stockSymbol, message);
        }
    }
}
