# @ohos.base

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
| [AsyncCallback](arkts-basicservices-asynccallback-t.md) | Defines a common callback that carries an error parameter and asynchronous return value.The error parameter is of the [BusinessError](arkts-basicservices-base-businesserror-i.md#BusinessError) type. The type of the asynchronous return value is defined by the developer. |
| [Callback](arkts-basicservices-callback-t.md) | Defines a common callback. You can set **data** to customize the data type of the information returned by the callback. |
| [ErrorCallback](arkts-basicservices-errorcallback-t.md) | Defines a common callback that carries an error parameter. The information returned by the callback is of the [BusinessError](arkts-basicservices-base-businesserror-i.md#BusinessError) type. |
| [RecordData](arkts-basicservices-recorddata-t.md) | RecordData is a union type used for object structures with uncertain levels and quantities at each level. |

