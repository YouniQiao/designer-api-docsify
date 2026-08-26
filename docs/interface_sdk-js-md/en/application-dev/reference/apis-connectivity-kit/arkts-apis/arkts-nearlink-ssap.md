# @ohos.nearlink.ssap(NearLink SSAP Connection Capability)

This module provides the SparkLink Service Access Protocol (SSAP) connection capability, including creating and connecting to a client, calling server methods, reading and writing descriptors, and subscribing to event notifications.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NearLink.Base

## Modules to Import

```TypeScript
import ssap from '@kit.ConnectivityKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createClient(NearLink SSAP Connection Capability)](arkts-connectivity-ssap-createclient-f.md) | Creates an SSAP client instance. |
| [createServer(NearLink SSAP Connection Capability)](arkts-connectivity-ssap-createserver-f.md) | Creates an SSAP server instance. |

### Interfaces

| Name | Description |
| --- | --- |
| [Client(NearLink SSAP Connection Capability)](arkts-connectivity-ssap-client-i.md) | Represents a SSAP client class. It provides APIs for connecting to and transmitting data with the server.Before using the methods of this class, use the [ssap.createClient](arkts-connectivity-ssap-createclient-f.md) method to construct an instance of this class.An app only needs to create one [Client](arkts-connectivity-ssap-client-i.md) instance for a remote device. Repeated creation will increase unnecessary resource overhead. |
| [ConnectionChangeState(NearLink SSAP Connection Capability)](arkts-connectivity-ssap-connectionchangestate-i.md) | Defines the connection status reporting parameters. |
| [Property(NearLink SSAP Connection Capability)](arkts-connectivity-ssap-property-i.md) | Represents a service Property. |
| [PropertyDescriptor(NearLink SSAP Connection Capability)](arkts-connectivity-ssap-propertydescriptor-i.md) | Defines the descriptor of a property. |
| [PropertyReadRequest(NearLink SSAP Connection Capability)](arkts-connectivity-ssap-propertyreadrequest-i.md) | Represents the Property read request parameter of the client. |
| [PropertyWriteRequest(NearLink SSAP Connection Capability)](arkts-connectivity-ssap-propertywriterequest-i.md) | Define a client property write request. |
| [Server(NearLink SSAP Connection Capability)](arkts-connectivity-ssap-server-i.md) | Represents a SSAP server class, which provides APIs for connecting to and exchanging data with the client.Before using the methods of this class, you need to call [ssap.createServer](arkts-connectivity-ssap-createserver-f.md) to create an instance of this class.An app only needs to create one [Server](arkts-connectivity-ssap-server-i.md) instance. Repeated creation will increase unnecessary resource overhead. |
| [ServerResponse(NearLink SSAP Connection Capability)](arkts-connectivity-ssap-serverresponse-i.md) | Defines a response to a client request. |
| [Service(NearLink SSAP Connection Capability)](arkts-connectivity-ssap-service-i.md) | Represents the NearLink service. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [Client(NearLink SSAP Connection Capability)](arkts-connectivity-ssap-client-i-sys.md) | Represents a SSAP client class. It provides APIs for connecting to and transmitting data with the server.Before using the methods of this class, use the [ssap.createClient](arkts-connectivity-ssap-createclient-f.md) method to construct an instance of this class.An app only needs to create one [Client](arkts-connectivity-ssap-client-i.md) instance for a remote device. Repeated creation will increase unnecessary resource overhead. |
| [Event(NearLink SSAP Connection Capability)](arkts-connectivity-ssap-event-i-sys.md) | Represents a service event. |
| [Method(NearLink SSAP Connection Capability)](arkts-connectivity-ssap-method-i-sys.md) | Represents a method of the service. |
| [Service(NearLink SSAP Connection Capability)](arkts-connectivity-ssap-service-i-sys.md) | Represents the NearLink service. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [Operation(NearLink SSAP Connection Capability)](arkts-connectivity-ssap-operation-e.md) | Enumerates the operation types supported by a property. |
| [PropertyDescriptorType(NearLink SSAP Connection Capability)](arkts-connectivity-ssap-propertydescriptortype-e.md) | Enumerates the property descriptor types. |
| [PropertyWriteType(NearLink SSAP Connection Capability)](arkts-connectivity-ssap-propertywritetype-e.md) | Enumerates the write types supported by a property. |

### Types

| Name | Description |
| --- | --- |
| [ConnectionState(NearLink SSAP Connection Capability)](arkts-connectivity-ssap-connectionstate-t.md) | Enumerates the connection states with a remote device. |
