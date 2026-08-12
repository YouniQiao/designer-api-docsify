# LazyForEach

For details about the development, see
[LazyForEach: Lazy Data Loading](docroot://ui/rendering-control/arkts-rendering-control-lazyforeach.md).

In scenarios involving a large number of child components, LazyForEach, when combined with techniques such as cached
list items, dynamic preloading, and component reuse, can significantly improve scrolling frame rates while reducing
memory usage. For best practices, see
[Optimizing Frame Loss for Long List Loading](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-best-practices-long-list).

## LazyForEach

```TypeScript
LazyForEach(
    dataSource: IDataSource,
    itemGenerator: (item: any, index: number) => void,
    keyGenerator?: (item: any, index: number) => string
  )
```

**LazyForEach** iterates over provided data sources and creates corresponding components during each iteration.When **LazyForEach** is used in a scrolling container, the framework creates components as required within the visible area of the scrolling container. When a component is out of the visible area, the framework destroys and reclaims the component to reduce memory usage.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LazyForEachInterface-(    dataSource: IDataSource,    itemGenerator: (item: any, index: number) => void,    keyGenerator?: (item: any, index: number) => string  ): LazyForEachAttribute--><!--Device-LazyForEachInterface-(    dataSource: IDataSource,    itemGenerator: (item: any, index: number) => void,    keyGenerator?: (item: any, index: number) => string  ): LazyForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataSource | [IDataSource](arkts-arkui-idatasource-i.md) | Yes |
| itemGenerator | (item: any, index: number) = & gt; void | Yes |
| keyGenerator | (item: any, index: number) = & gt; string | No |

## LazyForEach

```TypeScript
LazyForEach(
    dataSource: IDataSource,
    itemGenerator: (item: any, index: number) => void,
    keyGenerator?: (item: any, index: number) => string,
    options?: LazyForEachOptions
  )
```

Enter the value to obtain the LazyForEach.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LazyForEachInterface-(    dataSource: IDataSource,    itemGenerator: (item: any, index: number) => void,    keyGenerator?: (item: any, index: number) => string,    options?: LazyForEachOptions  ): LazyForEachAttribute--><!--Device-LazyForEachInterface-(    dataSource: IDataSource,    itemGenerator: (item: any, index: number) => void,    keyGenerator?: (item: any, index: number) => string,    options?: LazyForEachOptions  ): LazyForEachAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| dataSource | [IDataSource](arkts-arkui-idatasource-i.md) | Yes |
| itemGenerator | (item: any, index: number) = & gt; void | Yes |
| keyGenerator | (item: any, index: number) = & gt; string | No |
| options | [LazyForEachOptions](arkts-arkui-lazyforeachoptions-i.md) | No |

## Summary

- [DataAddOperation](arkts-arkui-lazyforeach-dataaddoperation-i.md)
- [DataChangeListener](arkts-arkui-lazyforeach-datachangelistener-i.md)
- [DataChangeOperation](arkts-arkui-lazyforeach-datachangeoperation-i.md)
- [DataDeleteOperation](arkts-arkui-lazyforeach-datadeleteoperation-i.md)
- [DataExchangeOperation](arkts-arkui-lazyforeach-dataexchangeoperation-i.md)
- [DataMoveOperation](arkts-arkui-lazyforeach-datamoveoperation-i.md)
- [DataReloadOperation](arkts-arkui-lazyforeach-datareloadoperation-i.md)
- [ExchangeIndex](arkts-arkui-lazyforeach-exchangeindex-i.md)
- [ExchangeKey](arkts-arkui-lazyforeach-exchangekey-i.md)
- [IDataSource](arkts-arkui-lazyforeach-idatasource-i.md)
- [LazyForEachOptions](arkts-arkui-lazyforeach-lazyforeachoptions-i.md)
- [MoveIndex](arkts-arkui-lazyforeach-moveindex-i.md)
- [DataOperation](arkts-arkui-lazyforeach-dataoperation-t.md)
- [DataOperationType](arkts-arkui-lazyforeach-dataoperationtype-e.md)
- [LazyForEachCustomComponentFreezeMode](arkts-arkui-lazyforeach-lazyforeachcustomcomponentfreezemode-e.md)
- [LazyForEachMemOptStrategy](arkts-arkui-lazyforeach-lazyforeachmemoptstrategy-e.md)
- [LazyForEachReleaseStrategy](arkts-arkui-lazyforeach-lazyforeachreleasestrategy-e.md)
