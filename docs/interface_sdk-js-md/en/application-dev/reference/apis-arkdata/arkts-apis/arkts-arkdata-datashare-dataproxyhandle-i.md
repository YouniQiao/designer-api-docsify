# DataProxyHandle

Defines the data proxy handle, which can be used to access or manage shared configuration information. Before calling an API provided by **DataProxyHandle**, you must create a **DataProxyHandle** instance using [createDataProxyHandle](arkts-arkdata-datashare-createdataproxyhandle-f.md).

**Since:** 20

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## Modules to Import

```TypeScript
import { dataShare } from 'kits/@kit.ArkData';
```

## delete

```TypeScript
delete(uris: string[], config: DataProxyConfig): Promise<DataProxyResult[]>
```

Deletes the specified shared configuration items based on URIs. This API uses a promise to return the result. Only the publisher is allowed to delete shared configuration items.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uris | string[] | Yes |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DataProxyResult](arkts-arkdata-datashare-dataproxyresult-i.md)[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [15700000](../errorcode-datashare.md#15700000-internal-error) |
| [15700014](../errorcode-datashare.md#15700014-incorrect-parameters-for-shared-configuration) |

## deleteMyPublishedData

```TypeScript
deleteMyPublishedData(config: DataProxyConfig): Promise<DataProxyResult[]>
```

Deletes all the data published by the publisher. Only the data publisher can delete the data.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DataProxyResult](arkts-arkdata-datashare-dataproxyresult-i.md)[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [15700000](../errorcode-datashare.md#15700000-internal-error) |
| [15700014](../errorcode-datashare.md#15700014-incorrect-parameters-for-shared-configuration) |

## get

```TypeScript
get(uris: string[], config: DataProxyConfig): Promise<DataProxyGetResult[]>
```

Obtains a specified shared configuration item based on the URI. This API uses a promise to return the result. Only the publisher and applications in the allowed list can access the shared configuration item.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uris | string[] | Yes |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DataProxyGetResult](arkts-arkdata-datashare-dataproxygetresult-i.md)[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [15700000](../errorcode-datashare.md#15700000-internal-error) |
| [15700014](../errorcode-datashare.md#15700014-incorrect-parameters-for-shared-configuration) |

## getValues

```TypeScript
getValues(uri: string, config: DataProxyConfig): Promise<ValueType[]>
```

Obtains all multi-value data under a specified URI. Only the publisher and the applications in the [allowList](arkts-arkdata-datashare-proxydata-i.md#allowlist) can obtain the data. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ValueType](arkts-arkdata-valuetype-t.md)[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [15700000](../errorcode-datashare.md#15700000-internal-error) |
| [15700011](../errorcode-datashare.md#15700011-uri-not-exist) |
| [15700014](../errorcode-datashare.md#15700014-incorrect-parameters-for-shared-configuration) |
| 15700015 |

## off

```TypeScript
off(
      event: 'dataChange',
      uris: string[],
      config: DataProxyConfig,
      callback?: AsyncCallback<DataProxyChangeInfo[]>
    ): DataProxyResult[]
```

Unsubscribes from the change event of the proxy data corresponding to a specified URI.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'dataChange' | Yes |
| uris | string[] | Yes |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DataProxyChangeInfo](arkts-arkdata-datashare-dataproxychangeinfo-i.md)[]&gt; | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataProxyResult](arkts-arkdata-datashare-dataproxyresult-i.md)[] |

**Error codes:**

| Error Code ID |
| --- |
| [15700000](../errorcode-datashare.md#15700000-internal-error) |
| [15700014](../errorcode-datashare.md#15700014-incorrect-parameters-for-shared-configuration) |

## on

```TypeScript
on(
      event: 'dataChange',
      uris: string[],
      config: DataProxyConfig,
      callback: AsyncCallback<DataProxyChangeInfo[]>
    ): DataProxyResult[]
```

Subscribes to the change event of the shared configuration corresponding to a specified URI. If the change event is subscribed, the subscriber will receive a callback notification that carries the data change type, changed URI, and changed content when the publisher modifies the configuration. This API uses an asynchronous callback to return the result. This function does not support cross-user notification subscription or subscription to unpublished configurations. If the permission is revoked after the subscription is successful, the subscriber will not be notified consequently.When the publisher calls the [publish](#publish) or [delete](#delete) API to publish or delete a configuration, a notification is automatically triggered.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | 'dataChange' | Yes |
| uris | string[] | Yes |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DataProxyChangeInfo](arkts-arkdata-datashare-dataproxychangeinfo-i.md)[]&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [DataProxyResult](arkts-arkdata-datashare-dataproxyresult-i.md)[] |

**Error codes:**

| Error Code ID |
| --- |
| [15700000](../errorcode-datashare.md#15700000-internal-error) |
| [15700014](../errorcode-datashare.md#15700014-incorrect-parameters-for-shared-configuration) |

## publish

```TypeScript
publish(data: ProxyData[], config: DataProxyConfig): Promise<DataProxyResult[]>
```

Publishes shared configuration items. This API uses a promise to return the result. After shared configuration items are published, the publisher and the applications in the allowlist can access these items. If the URI to be published already exists, the corresponding shared configuration item is updated. If any URI in the configuration item to be published exceeds the maximum length or fails the format verification, the current publish operation fails. Only the publisher can update shared configuration items. Each application supports a maximum of 32 shared configurations.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | [ProxyData[]](arkts-arkdata-datashare-proxydata-i.md) | Yes |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[DataProxyResult](arkts-arkdata-datashare-dataproxyresult-i.md)[]&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [15700000](../errorcode-datashare.md#15700000-internal-error) |
| [15700014](../errorcode-datashare.md#15700014-incorrect-parameters-for-shared-configuration) |

## putValue

```TypeScript
putValue(uri: string, key: number, value: ValueType, config: DataProxyConfig): Promise<void>
```

Puts a value into the published data. This operation can be performed only on multi-value type data. If the input **key** does not exist, a new value is added. If the input **key** already exists, the value corresponding to the key is updated. By default, a maximum of 10 values can be added to a single data record (that is, a URI) for a single application, and the maximum length of each value is 4096 bytes. In addition, the total length of all values in a single data record is limited by the value of the **maxValueLength** parameter that is specified during data publishing. Note that the **maxValueLength** parameter does not take effect in this API. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| key | number | Yes |
| value | [ValueType](arkts-arkdata-valuetype-t.md) | Yes |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [15700000](../errorcode-datashare.md#15700000-internal-error) |
| [15700011](../errorcode-datashare.md#15700011-uri-not-exist) |
| [15700014](../errorcode-datashare.md#15700014-incorrect-parameters-for-shared-configuration) |
| 15700015 |

## removeValue

```TypeScript
removeValue(uri: string, key: number, config: DataProxyConfig): Promise<void>
```

Removes the value corresponding to the key. This operation can be performed only on multi-value type data. Only values added by this application can be removed. This API uses a promise to return the result.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uri | string | Yes |
| key | number | Yes |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [15700000](../errorcode-datashare.md#15700000-internal-error) |
| [15700011](../errorcode-datashare.md#15700011-uri-not-exist) |
| [15700014](../errorcode-datashare.md#15700014-incorrect-parameters-for-shared-configuration) |
| 15700015 |
