package code.java.stock;

// 主题接口
interface Topic {
    void receiveUpdate(String stockSymbol, String message);
    void subscribe(Subscriber subscriber);
    void unsubscribe(Subscriber subscriber);
}

// 具体主题
class ConcreteTopic implements Topic {
    private TopicObserver observer = new TopicObserver();

    private String lastestStockMessage = "";

    public void setLastestStockMessage(String lastestStockMessage) {
        this.lastestStockMessage = lastestStockMessage;
        observer.notifySubscribers(lastestStockMessage);
    }

    // 当topicObserver监听到topic发生变化时，将这个变化发送给订阅者
    @Override
    public void receiveUpdate(String stockSymbol, String message) {
        setLastestStockMessage(message);
    }

    public void subscribe(Subscriber subscriber) {
        observer.addSubscriber(subscriber);
    }

    public void unsubscribe(Subscriber subscriber) {
        observer.removeSubscriber(subscriber);
    }
}