# Client

管理SSAP客户端。在调用ssap客户端方法之前，必须使用{@link createClient}创建ssap客户端实例。

**起始版本：** 26.0.0

<!--Device-ssap-interface Client--><!--Device-ssap-interface Client-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

## close

```TypeScript
close(): void
```

关闭客户端。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Client-close(): void--><!--Device-Client-close(): void-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**错误码：**

| 错误码ID |
| --- |
| [36100003](../errorcode-nearlink-service.md#36100003--星闪关闭) |
| [36100099](../errorcode-nearlink-service.md#36100099-操作失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## connect

```TypeScript
connect(): Promise<void>
```

连接服务端。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Client-connect(): Promise<void>--><!--Device-Client-connect(): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [36100003](../errorcode-nearlink-service.md#36100003--星闪关闭) |
| [36100099](../errorcode-nearlink-service.md#36100099-操作失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## disconnect

```TypeScript
disconnect(): Promise<void>
```

断开或停止与服务端的连接。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Client-disconnect(): Promise<void>--><!--Device-Client-disconnect(): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [36100003](../errorcode-nearlink-service.md#36100003--星闪关闭) |
| [36100099](../errorcode-nearlink-service.md#36100099-操作失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## getServices

```TypeScript
getServices(): Promise<Service[]>
```

开始发现服务端的所有服务。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Client-getServices(): Promise<Service[]>--><!--Device-Client-getServices(): Promise<Service[]>-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**返回值：**

| 类型 |
| --- |
| Promise&lt;Service[]&gt; |

**错误码：**

| 错误码ID |
| --- |
| [36100003](../errorcode-nearlink-service.md#36100003--星闪关闭) |
| [36100099](../errorcode-nearlink-service.md#36100099-操作失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## offConnectionStateChange

```TypeScript
offConnectionStateChange(callback?: Callback<ConnectionChangeState>): void
```

取消订阅客户端连接状态更改事件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Client-offConnectionStateChange(callback?: Callback<ConnectionChangeState>): void--><!--Device-Client-offConnectionStateChange(callback?: Callback<ConnectionChangeState>): void-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ConnectionChangeState&gt; | 否 |

## offMtuChange

```TypeScript
offMtuChange(callback?: Callback<number>): void
```

取消订阅MTU更改事件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Client-offMtuChange(callback?: Callback<int>): void--><!--Device-Client-offMtuChange(callback?: Callback<int>): void-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 否 |

## offPropertyChange

```TypeScript
offPropertyChange(callback?: Callback<Property>): void
```

取消订阅属性值更改事件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Client-offPropertyChange(callback?: Callback<Property>): void--><!--Device-Client-offPropertyChange(callback?: Callback<Property>): void-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Property&gt; | 否 |

## onConnectionStateChange

```TypeScript
onConnectionStateChange(callback: Callback<ConnectionChangeState>): void
```

订阅客户端连接状态更改事件。

只有授予了ohos.permission.NEARLINK_ACCESS权限的应用程序才能访问此事件。如果应用被赋予了ohos.permission.GET_NEARLINK_PEER_MAC权限。回调返回真实设备地址，否则返回随机设备地址。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Client-onConnectionStateChange(callback: Callback<ConnectionChangeState>): void--><!--Device-Client-onConnectionStateChange(callback: Callback<ConnectionChangeState>): void-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ConnectionChangeState&gt; | 是 |

## onMtuChange

```TypeScript
onMtuChange(callback: Callback<number>): void
```

订阅MTU变化事件。

只有授予了ohos.permission.NEARLINK_ACCESS权限的应用程序才能访问此事件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Client-onMtuChange(callback: Callback<int>): void--><!--Device-Client-onMtuChange(callback: Callback<int>): void-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;number&gt; | 是 |

## onPropertyChange

```TypeScript
onPropertyChange(callback: Callback<Property>): void
```

订阅属性值变更事件。

只有授予了ohos.permission.NEARLINK_ACCESS权限的应用程序才能访问此事件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Client-onPropertyChange(callback: Callback<Property>): void--><!--Device-Client-onPropertyChange(callback: Callback<Property>): void-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Property&gt; | 是 |

## readProperty

```TypeScript
readProperty(property: Property): Promise<Property>
```

读取服务端的属性。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Client-readProperty(property: Property): Promise<Property>--><!--Device-Client-readProperty(property: Property): Promise<Property>-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| property | [Property](arkts-connectivity-ssap-property-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Property&gt; |

**错误码：**

| 错误码ID |
| --- |
| [36100003](../errorcode-nearlink-service.md#36100003--星闪关闭) |
| [36100099](../errorcode-nearlink-service.md#36100099-操作失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [36100044](../errorcode-nearlink-service.md#36100044-禁止使用星闪标准服务uuid) |
| [36100043](../errorcode-nearlink-service.md#36100043-无效uuid) |

## requestMtuSize

```TypeScript
requestMtuSize(mtu: number): Promise<void>
```

与服务端协商MTU大小。协商结果需要通过订阅MTU事件获取。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Client-requestMtuSize(mtu: int): Promise<void>--><!--Device-Client-requestMtuSize(mtu: int): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mtu | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [36100003](../errorcode-nearlink-service.md#36100003--星闪关闭) |
| [36100099](../errorcode-nearlink-service.md#36100099-操作失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## setPropertyNotification

```TypeScript
setPropertyNotification(property: Property, enable: boolean): Promise<void>
```

启用或禁用属性值变更通知。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Client-setPropertyNotification(property: Property, enable: boolean): Promise<void>--><!--Device-Client-setPropertyNotification(property: Property, enable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| property | [Property](arkts-connectivity-ssap-property-i.md) | 是 |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [36100003](../errorcode-nearlink-service.md#36100003--星闪关闭) |
| [36100099](../errorcode-nearlink-service.md#36100099-操作失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [36100044](../errorcode-nearlink-service.md#36100044-禁止使用星闪标准服务uuid) |
| [36100043](../errorcode-nearlink-service.md#36100043-无效uuid) |

## writeProperty

```TypeScript
writeProperty(property: Property, writeType: PropertyWriteType): Promise<void>
```

写入服务端的属性。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Client-writeProperty(property: Property, writeType: PropertyWriteType): Promise<void>--><!--Device-Client-writeProperty(property: Property, writeType: PropertyWriteType): Promise<void>-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| property | [Property](arkts-connectivity-ssap-property-i.md) | 是 |
| writeType | [PropertyWriteType](arkts-connectivity-ssap-propertywritetype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [36100003](../errorcode-nearlink-service.md#36100003--星闪关闭) |
| [36100099](../errorcode-nearlink-service.md#36100099-操作失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [36100044](../errorcode-nearlink-service.md#36100044-禁止使用星闪标准服务uuid) |
| [36100043](../errorcode-nearlink-service.md#36100043-无效uuid) |
