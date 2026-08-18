# AsyncCallback(Public Callback Information)

Defines a common callback that carries an error parameter and asynchronous return value. It is used to return error information or success data when an asynchronous operation is complete. The error parameter is of the [BusinessError](arkts-basicservices-base-businesserror-i.md#businesserror) type. The type of the asynchronous return value is defined by the developer.

**Since:** 6

<!--Device-unnamed-export interface AsyncCallback--><!--Device-unnamed-export interface AsyncCallback-End-->

**System capability:** SystemCapability.Base

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
(err: BusinessError<E>, data: T): void
```

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-AsyncCallback-(err: BusinessError<E>, data: T): void--><!--Device-AsyncCallback-(err: BusinessError<E>, data: T): void-End-->

**System capability:** SystemCapability.Base

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| err | [BusinessError](arkts-basicservices-base-businesserror-i.md)&lt;E&gt; | Yes |
| data | T | Yes |
