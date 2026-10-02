import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

@Service
public class StockService {

    private static final Logger log =
            LoggerFactory.getLogger(StockService.class);

    public void processStock(String symbol) {

        log.info("Processing stock symbol={}", symbol);

        try {
            // business logic

            log.debug("Stock processing completed symbol={}", symbol);

        } catch (Exception ex) {

            log.error(
                    "Stock processing failed symbol={}",
                    symbol,
                    ex
            );

            throw ex;
        }
    }
}