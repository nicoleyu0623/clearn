package io.axoniq.training.labs.giftcard.gui;

import com.vaadin.annotations.Push;
import com.vaadin.server.VaadinRequest;
import com.vaadin.spring.annotation.SpringUI;
import com.vaadin.ui.Button;
import com.vaadin.ui.FormLayout;
import com.vaadin.ui.HorizontalLayout;
import com.vaadin.ui.Notification;
import com.vaadin.ui.Panel;
import com.vaadin.ui.TextField;
import com.vaadin.ui.UI;
import com.vaadin.ui.VerticalLayout;
import io.axoniq.training.labs.giftcard.coreapi.IssueCardCommand;
import io.axoniq.training.labs.giftcard.coreapi.RedeemCardCommand;
import io.axoniq.training.labs.giftcard.coreapi.ReimburseCardCommand;
import org.axonframework.commandhandling.gateway.CommandGateway;

import java.util.UUID;

@SpringUI
@Push
public class GiftCardUI extends UI {

    private final CommandGateway commandGateway;

    public GiftCardUI(CommandGateway commandGateway) {
        this.commandGateway = commandGateway;
    }

    @Override
    protected void init(VaadinRequest vaadinRequest) {
        HorizontalLayout commandBar = new HorizontalLayout(
                issuePanel(), bulkIssuePanel(), redeemPanel(), reimbursePanel()
        );
        commandBar.setSizeFull();

        VerticalLayout layout = new VerticalLayout(commandBar);
        layout.setSizeFull();

        getUI().setErrorHandler(event -> {
            Throwable cause = event.getThrowable();
            while (cause.getCause() != null) {
                cause = cause.getCause();
            }
            Notification.show("Error", cause.getMessage(), Notification.Type.ERROR_MESSAGE);
        });
        setContent(layout);
    }

    private Panel issuePanel() {
        TextField id = new TextField("Card id");
        TextField amount = new TextField("Amount");
        Button submit = new Button("Submit", evt -> {
            commandGateway.sendAndWait(new IssueCardCommand(id.getValue(), Integer.parseInt(amount.getValue())));
            Notification.show("Success", Notification.Type.HUMANIZED_MESSAGE);
        });

        FormLayout form = new FormLayout(id, amount, submit);
        form.setMargin(true);

        return new Panel("Issue single card", form);
    }

    private Panel bulkIssuePanel() {
        TextField number = new TextField("Number");
        TextField amount = new TextField("Amount");
        Button submit = new Button("Submit", evt -> {
            for (int i = 0; i < Integer.parseInt(number.getValue()); i++) {
                String id = UUID.randomUUID().toString().substring(0, 11).toUpperCase();
                commandGateway.sendAndWait(new IssueCardCommand(id, Integer.parseInt(amount.getValue())));
            }
            Notification.show("Success", Notification.Type.HUMANIZED_MESSAGE);
        });

        FormLayout form = new FormLayout(number, amount, submit);
        form.setMargin(true);

        Panel panel = new Panel("Bulk issue cards");
        panel.setContent(form);
        return panel;
    }

    private Panel redeemPanel() {
        TextField id = new TextField("Card ID");
        TextField txId = new TextField("TransactionID");
        TextField amount = new TextField("Amount");
        Button submit = new Button("Submit", evt -> {
            int parsedAmount = Integer.parseInt(amount.getValue());
            commandGateway.sendAndWait(new RedeemCardCommand(id.getValue(), txId.getValue(), parsedAmount));
            Notification.show("Success", Notification.Type.HUMANIZED_MESSAGE);
        });

        FormLayout form = new FormLayout();
        form.addComponents(id, txId, amount, submit);
        form.setMargin(true);

        return new Panel("Redeem card", form);
    }

    private Panel reimbursePanel() {
        TextField id = new TextField("Card ID");
        TextField txId = new TextField("TransactionID");
        Button submit = new Button("Submit", evt -> {
            commandGateway.sendAndWait(new ReimburseCardCommand(id.getValue(), txId.getValue()));
            Notification.show("Success", Notification.Type.HUMANIZED_MESSAGE);
        });

        FormLayout form = new FormLayout();
        form.addComponents(id, txId, submit);
        form.setMargin(true);

        return new Panel("Reimburse card", form);
    }
}
