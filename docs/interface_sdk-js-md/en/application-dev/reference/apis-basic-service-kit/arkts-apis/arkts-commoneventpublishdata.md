# commonEventPublishData

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [CommonEventPublishData](arkts-basicservices-commoneventpublishdata-commoneventpublishdata-i.md) | This module encapsulates the data and attributes carried when a common event is published, including the event data (code/data), subscriber permissions, subscriber bundle name, whether the event is ordered or sticky, and additional parameters. It allows the publisher to precisely control the common event recipients, event delivery sequence, and sticky feature. This module is applicable to scenarios where the recipients need to be specified, custom event data needs to be transferred, and ordered/sticky common events need to be implemented. > **NOTE：**> > If there is no restriction, any app can subscribe to common events and read the > information carried by the event. In this case, sensitive information should not be > carried in common events. The **subscriberPermissions** and **bundleName** parameters > of this module can be used to restrict the receiving scope of common events. |

