# @ohos.base

The **Base** module defines the public callback types of ArkTS APIs, including the common and error callbacks.
 > **NOTE**
 >
 > - The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a
 >   superscript to indicate their earliest API version.
 >
 > - Since API version 12, the APIs of this module are supported in ArkTS widgets.


## Modules to Import

```TypeScript
import { Callback, BusinessError, ErrorCallback, AsyncCallback } from '@kit.BasicServicesKit';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [BusinessError](arkts-basicservices-base-businesserror-c.md) | Defines the error parameter. |

### Types

| Name | Description |
| --- | --- |
| [AsyncCallback](arkts-basicservices-asynccallback-t.md) | Defines a common callback that carries an error parameter and asynchronous return value.The error parameter is of the [BusinessError](arkts-basicservices-base-businesserror-c.md#BusinessError) type. The type of the asynchronous return value is defined by the developer. |
| [Callback](arkts-basicservices-callback-t.md) | Defines a common callback. You can set **data** to customize the data type of the information returned by the callback. |
| [ErrorCallback](arkts-basicservices-errorcallback-t.md) | Defines a common callback that carries an error parameter. The information returned by the callback is of the [BusinessError](arkts-basicservices-base-businesserror-c.md#BusinessError) type. |
| [RecordData](arkts-basicservices-recorddata-t.md) | RecordData is a union type used for object structures with uncertain levels and quantities at each level. |

