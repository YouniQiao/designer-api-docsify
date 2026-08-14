# DataProxyHandle

Defines the data proxy handle, which can be used to access or manage shared configuration information. Before calling an API provided by **DataProxyHandle**, you must create a **DataProxyHandle** instance using [createDataProxyHandle](arkts-arkdata-datashare-createdataproxyhandle-f.md#createDataProxyHandle).

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-dataShare-interface DataProxyHandle--><!--Device-dataShare-interface DataProxyHandle-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## Modules to Import

```TypeScript
import { dataShare } from 'dataShare';
```

## delete

```TypeScript
delete(uris: string[], config: DataProxyConfig): Promise<DataProxyResult[]>
```

Deletes the specified shared configuration items based on URIs. This API uses a promise to return the result. Only the publisher is allowed to delete shared configuration items.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyHandle-delete(uris: string[], config: DataProxyConfig): Promise<DataProxyResult[]>--><!--Device-DataProxyHandle-delete(uris: string[], config: DataProxyConfig): Promise<DataProxyResult[]>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uris | string[] | Yes | URI array of the shared configuration items to be deleted, with a maximum of 32 URIs. The URI value is fixed at the format of **"datashareproxy://{*bundleName*}/{*path*}"**, in which **bundleName** indicates the bundle name of the publisher application, and **path** can be set to any value but must be unique in the same application. The value contains a maximum of 256 bytes. |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | Yes | Data proxy configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[DataProxyResult](arkts-arkdata-datashare-dataproxyresult-i.md)[]&gt; | Promise used to return the result array of the batch operations. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [15700014](../errorcode-datashare.md#15700014-incorrect-parameters-for-shared-configuration) | The parameter format is incorrect or the value range is invalid. |
| [15700000](../errorcode-datashare.md#15700000-internal-error) | Inner error. Possible causes: The service is not ready or is being restarted abnormally. |

## Examples

```TypeScript
const urisToDelete: string[] =
  ['datashareproxy://com.example.app1/config1', 'datashareproxy://com.example.app1/config2',];
const config: dataShare.DataProxyConfig = {
  type: dataShare.DataProxyType.SHARED_CONFIG,
};
dataProxyHandle.delete(urisToDelete, config).then((results: dataShare.DataProxyResult[]) => {
  results.forEach((result) => {
    console.info(`URI: ${result.uri}, Result: ${result.result}`);
  });
}).catch((error: BusinessError) => {
  console.error('Error deleting config:', error);
});
```

## deleteMyPublishedData

```TypeScript
deleteMyPublishedData(config: DataProxyConfig): Promise<DataProxyResult[]>
```

Deletes all the data published by the publisher. Only the data publisher can delete the data.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyHandle-deleteMyPublishedData(config: DataProxyConfig): Promise<DataProxyResult[]>--><!--Device-DataProxyHandle-deleteMyPublishedData(config: DataProxyConfig): Promise<DataProxyResult[]>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | Yes | Configuration of the data proxy operation. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[DataProxyResult](arkts-arkdata-datashare-dataproxyresult-i.md)[]&gt; | Promise used to return the operation result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [15700014](../errorcode-datashare.md#15700014-incorrect-parameters-for-shared-configuration) | The parameter format is incorrect or the value range is invalid. |
| [15700000](../errorcode-datashare.md#15700000-internal-error) | Inner error. Possible causes: The service is not ready or is being restarted abnormally. |

## get

```TypeScript
get(uris: string[], config: DataProxyConfig): Promise<DataProxyGetResult[]>
```

Obtains a specified shared configuration item based on the URI. This API uses a promise to return the result. Only the publisher and applications in the allowed list can access the shared configuration item.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyHandle-get(uris: string[], config: DataProxyConfig): Promise<DataProxyGetResult[]>--><!--Device-DataProxyHandle-get(uris: string[], config: DataProxyConfig): Promise<DataProxyGetResult[]>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uris | string[] | Yes | URI array of the shared configuration items to be obtained, with a maximum of 32 URIs. The URI value is fixed at the format of **"datashareproxy://{*bundleName*}/{*path*}"**, in which **bundleName** indicates the bundle name of the publisher application, and **path** can be set to any value but must be unique in the same application. The value contains a maximum of 256 bytes. |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | Yes | Data proxy configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[DataProxyGetResult](arkts-arkdata-datashare-dataproxygetresult-i.md)[]&gt; | Promise used to return the result array of the batch operations. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [15700014](../errorcode-datashare.md#15700014-incorrect-parameters-for-shared-configuration) | The parameter format is incorrect or the value range is invalid. |
| [15700000](../errorcode-datashare.md#15700000-internal-error) | Inner error. Possible causes: The service is not ready or is being restarted abnormally. |

## Examples

```TypeScript
const urisToGet: string[] =
  ['datashareproxy://com.example.app1/config1', 'datashareproxy://com.example.app1/config2',];
const config: dataShare.DataProxyConfig = {
  type: dataShare.DataProxyType.SHARED_CONFIG,
};
dataProxyHandle.get(urisToGet, config).then((results: dataShare.DataProxyGetResult[]) => {
  results.forEach((result) => {
    console.info(`URI: ${result.uri}, Result: ${result.result}, AllowList: ${result.allowList}`);
  });
}).catch((error: BusinessError) => {
  console.error('Error getting config:', error);
});
```

## getValues

```TypeScript
getValues(uri: string, config: DataProxyConfig): Promise<ValueType[]>
```

Obtains all multi-value data under a specified URI. Only the publisher and the applications in the [allowList](arkts-arkdata-datashare-proxydata-i.md#allowList) can obtain the data. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyHandle-getValues(uri: string, config: DataProxyConfig): Promise<ValueType[]>--><!--Device-DataProxyHandle-getValues(uri: string, config: DataProxyConfig): Promise<ValueType[]>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | Indicates the URI of the data to operate. |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | Yes | Configuration of the data proxy operation. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ValueType](arkts-arkdata-valuetype-t.md)[]&gt; | Promise used to return an array of all values under the URI. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15700015 | No permission to access the data specified by the URI. |
| [15700014](../errorcode-datashare.md#15700014-incorrect-parameters-for-shared-configuration) | The parameter format is incorrect or the value range is invalid. |
| [15700011](../errorcode-datashare.md#15700011-uri-not-exist) | The URI does not exist. |
| [15700000](../errorcode-datashare.md#15700000-internal-error) | Inner error. Possible causes: The service is not ready or is being restarted abnormally. |

## offDataChange

```TypeScript
offDataChange(
      uris: string[],
      config: DataProxyConfig,
      callback?: Callback<DataProxyChangeInfo[]>
    ): DataProxyResult[]
```

Deregisters observers to observe proxy data change specified by the given URIs.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyHandle-offDataChange(      uris: string[],      config: DataProxyConfig,      callback?: Callback<DataProxyChangeInfo[]>    ): DataProxyResult[]--><!--Device-DataProxyHandle-offDataChange(      uris: string[],      config: DataProxyConfig,      callback?: Callback<DataProxyChangeInfo[]>    ): DataProxyResult[]-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uris | string[] | Yes | Indicates the uris of the data to operate. |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | Yes | Indicates the configuration of the data proxy operation. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataProxyChangeInfo](arkts-arkdata-datashare-dataproxychangeinfo-i.md)[]&gt; | No | The callback function when data changes. |

**Return value:**

| Type | Description |
| --- | --- |
| [DataProxyResult](arkts-arkdata-datashare-dataproxyresult-i.md)[] | : The operation result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [15700014](../errorcode-datashare.md#15700014-incorrect-parameters-for-shared-configuration) | The parameter format is incorrect or the value range is invalid. |
| [15700000](../errorcode-datashare.md#15700000-internal-error) | Inner error. Possible causes: The service is not ready or is being restarted abnormally. |

## off_dataChange

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

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyHandle-off(      event: 'dataChange',      uris: string[],      config: DataProxyConfig,      callback?: AsyncCallback<DataProxyChangeInfo[]>    ): DataProxyResult[]--><!--Device-DataProxyHandle-off(      event: 'dataChange',      uris: string[],      config: DataProxyConfig,      callback?: AsyncCallback<DataProxyChangeInfo[]>    ): DataProxyResult[]-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'dataChange' | Yes | Event or callback type. The value is **dataChange**, which indicates the data change. |
| uris | string[] | Yes | Array of URIs to be unsubscribed, with a maximum of 32 URIs. The URI value is fixed at the format of **"datashareproxy://{*bundleName*}/{*path*}"**, in which **bundleName** indicates the bundle name of the publisher application, and **path** can be set to any value but must be unique in the same application. The value contains a maximum of 256 bytes. |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | Yes | Data proxy configuration. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DataProxyChangeInfo](arkts-arkdata-datashare-dataproxychangeinfo-i.md)[]&gt; | No | Callback function. If the value is empty, undefined, or null, all notifications of the URIs are unsubscribed. |

**Return value:**

| Type | Description |
| --- | --- |
| [DataProxyResult](arkts-arkdata-datashare-dataproxyresult-i.md)[] | Batch operation result array. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [15700014](../errorcode-datashare.md#15700014-incorrect-parameters-for-shared-configuration) | The parameter format is incorrect or the value range is invalid. |
| [15700000](../errorcode-datashare.md#15700000-internal-error) | Inner error. Possible causes: The service is not ready or is being restarted abnormally. |

## Examples

```TypeScript
const urisToUnWatch: string[] =
  ['datashareproxy://com.example.app1/config1', 'datashareproxy://com.example.app1/config2',];
const config: dataShare.DataProxyConfig = {
  type: dataShare.DataProxyType.SHARED_CONFIG,
};
const callback = (err: BusinessError<void>, changes: dataShare.DataProxyChangeInfo[]): void => {
  if (err) {
    console.error('err:', err);
  } else {
    changes.forEach((change) => {
      console.info(`Change Type: ${change.type}, URI: ${change.uri}, Value: ${change.value}`);
    });
  }
};
const results: dataShare.DataProxyResult[] = dataProxyHandle.off('dataChange', urisToUnWatch, config, callback);
results.forEach((result) => {
  console.info(`URI: ${result.uri}, Result: ${result.result}`);
});
```

## onDataChange

```TypeScript
onDataChange(
      uris: string[],
      config: DataProxyConfig,
      callback: Callback<DataProxyChangeInfo[]>
    ): DataProxyResult[]
```

Registers observers to observe proxy data change specified by the given URIs.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyHandle-onDataChange(      uris: string[],      config: DataProxyConfig,      callback: Callback<DataProxyChangeInfo[]>    ): DataProxyResult[]--><!--Device-DataProxyHandle-onDataChange(      uris: string[],      config: DataProxyConfig,      callback: Callback<DataProxyChangeInfo[]>    ): DataProxyResult[]-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uris | string[] | Yes | Indicates the uris of the data to operate. |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | Yes | Indicates the configuration of the data proxy operation. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataProxyChangeInfo](arkts-arkdata-datashare-dataproxychangeinfo-i.md)[]&gt; | Yes | The callback function when data changes. |

**Return value:**

| Type | Description |
| --- | --- |
| [DataProxyResult](arkts-arkdata-datashare-dataproxyresult-i.md)[] | : The operation result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [15700014](../errorcode-datashare.md#15700014-incorrect-parameters-for-shared-configuration) | The parameter format is incorrect or the value range is invalid. |
| [15700000](../errorcode-datashare.md#15700000-internal-error) | Inner error. Possible causes: The service is not ready or is being restarted abnormally. |

## on_dataChange

```TypeScript
on(
      event: 'dataChange',
      uris: string[],
      config: DataProxyConfig,
      callback: AsyncCallback<DataProxyChangeInfo[]>
    ): DataProxyResult[]
```

Subscribes to the change event of the shared configuration corresponding to a specified URI. If the change event is subscribed, the subscriber will receive a callback notification that carries the data change type, changed URI , and changed content when the publisher modifies the configuration. This API uses an asynchronous callback to return the result. This function does not support cross-user notification subscription or subscription to unpublished configurations. If the permission is revoked after the subscription is successful, the subscriber will not be notified consequently. When the publisher calls the [publish](#publish) or [delete](#delete) API to publish or delete a configuration, a notification is automatically triggered.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyHandle-on(      event: 'dataChange',      uris: string[],      config: DataProxyConfig,      callback: AsyncCallback<DataProxyChangeInfo[]>    ): DataProxyResult[]--><!--Device-DataProxyHandle-on(      event: 'dataChange',      uris: string[],      config: DataProxyConfig,      callback: AsyncCallback<DataProxyChangeInfo[]>    ): DataProxyResult[]-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | 'dataChange' | Yes | Event or callback type. The value is **dataChange**, which indicates the data change. This event is triggered when the publisher modifies the configuration. |
| uris | string[] | Yes | Array of URIs to be subscribed, with a maximum of 32 URIs. The URI value is fixed at the format of **"datashareproxy://{*bundleName*}/{*path*}"**, in which **bundleName** indicates the bundle name of the publisher application, and **path** can be set to any value but must be unique in the same application. The value contains a maximum of 256 bytes. |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | Yes | Data proxy configuration. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[DataProxyChangeInfo](arkts-arkdata-datashare-dataproxychangeinfo-i.md)[]&gt; | Yes | Callback triggered when the publisher modifies the configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| [DataProxyResult](arkts-arkdata-datashare-dataproxyresult-i.md)[] | Batch operation result array. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [15700014](../errorcode-datashare.md#15700014-incorrect-parameters-for-shared-configuration) | The parameter format is incorrect or the value range is invalid. |
| [15700000](../errorcode-datashare.md#15700000-internal-error) | Inner error. Possible causes: The service is not ready or is being restarted abnormally. |

## Examples

```TypeScript
const urisToWatch: string[] =
  ['datashareproxy://com.example.app1/config1', 'datashareproxy://com.example.app1/config2',];
const config: dataShare.DataProxyConfig = {
  type: dataShare.DataProxyType.SHARED_CONFIG,
};
const callback = (err: BusinessError<void>, changes: dataShare.DataProxyChangeInfo[]): void => {
  if (err) {
    console.error('err:', err);
  } else {
    changes.forEach((change) => {
      console.info(`Change Type: ${change.type}, URI: ${change.uri}, Value: ${change.value}`);
    });
  }
};
const results: dataShare.DataProxyResult[] = dataProxyHandle.on('dataChange', urisToWatch, config, callback);
results.forEach((result) => {
  console.info(`URI: ${result.uri}, Result: ${result.result}`);
});
```

## publish

```TypeScript
publish(data: ProxyData[], config: DataProxyConfig): Promise<DataProxyResult[]>
```

Publishes shared configuration items. This API uses a promise to return the result. After shared configuration items are published, the publisher and the applications in the allowlist can access these items. If the URI to be published already exists, the corresponding shared configuration item is updated. If any URI in the configuration item to be published exceeds the maximum length or fails the format verification, the current publish operation fails. Only the publisher can update shared configuration items. Each application supports a maximum of 32 shared configurations.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyHandle-publish(data: ProxyData[], config: DataProxyConfig): Promise<DataProxyResult[]>--><!--Device-DataProxyHandle-publish(data: ProxyData[], config: DataProxyConfig): Promise<DataProxyResult[]>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | ProxyData[] | Yes | Array of shared configuration items to be created or updated, with a maximum of 32 items. |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | Yes | Data proxy configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[DataProxyResult](arkts-arkdata-datashare-dataproxyresult-i.md)[]&gt; | Promise used to return the result array of the batch operations. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [15700014](../errorcode-datashare.md#15700014-incorrect-parameters-for-shared-configuration) | The parameter format is incorrect or the value range is invalid. |
| [15700000](../errorcode-datashare.md#15700000-internal-error) | Inner error. Possible causes: The service is not ready or is being restarted abnormally. |

## Examples

```TypeScript
const newConfigData: dataShare.ProxyData[] = [{
  uri: 'datashareproxy://com.example.app1/config1',
  value: 'Value1',
  allowList: ['appIdentifier2', 'appIdentifier3'], // This string is for reference only. Replace it with the actual application identifier.
}, {
  uri: 'datashareproxy://com.example.app1/config2',
  value: 'Value2',
  allowList: ['appIdentifier3', 'appIdentifier4'], // This string is for reference only. Replace it with the actual application identifier.
}];
const config: dataShare.DataProxyConfig = {
  type: dataShare.DataProxyType.SHARED_CONFIG,
};
dataProxyHandle.publish(newConfigData, config).then((results: dataShare.DataProxyResult[]) => {
  results.forEach((result) => {
    console.info(`URI: ${result.uri}, Result: ${result.result}`);
  });
}).catch((error: BusinessError) => {
  console.error('Error publishing config:', error);
});
```

## putValue

```TypeScript
putValue(uri: string, key: int, value: ValueType, config: DataProxyConfig): Promise<void>
```

Puts a value into the published data. This operation can be performed only on multi-value type data. If the input **key** does not exist, a new value is added. If the input **key** already exists, the value corresponding to the key is updated. By default, a maximum of 10 values can be added to a single data record (that is, a URI) for a single application, and the maximum length of each value is 4096 bytes. In addition, the total length of all values in a single data record is limited by the value of the **maxValueLength** parameter that is specified during data publishing. Note that the **maxValueLength** parameter does not take effect in this API. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyHandle-putValue(uri: string, key: int, value: ValueType, config: DataProxyConfig): Promise<void>--><!--Device-DataProxyHandle-putValue(uri: string, key: int, value: ValueType, config: DataProxyConfig): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | Indicates the URI of the data to operate. |
| key | int | Yes | The key corresponding to the added value. It is unique for the same application. <br>The value range is all integers. |
| value | [ValueType](arkts-arkdata-valuetype-t.md) | Yes | The value to be put. |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | Yes | Configuration of the data proxy operation. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15700015 | No permission to access the data specified by the URI. |
| [15700014](../errorcode-datashare.md#15700014-incorrect-parameters-for-shared-configuration) | The parameter format is incorrect or the value range is invalid. |
| [15700011](../errorcode-datashare.md#15700011-uri-not-exist) | The URI does not exist. |
| [15700000](../errorcode-datashare.md#15700000-internal-error) | Inner error. Possible causes: The service is not ready or is being restarted abnormally. |

## removeValue

```TypeScript
removeValue(uri: string, key: int, config: DataProxyConfig): Promise<void>
```

Removes the value corresponding to the key. This operation can be performed only on multi-value type data. Only values added by this application can be removed. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-DataProxyHandle-removeValue(uri: string, key: int, config: DataProxyConfig): Promise<void>--><!--Device-DataProxyHandle-removeValue(uri: string, key: int, config: DataProxyConfig): Promise<void>-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uri | string | Yes | Indicates the URI of the data to operate. |
| key | int | Yes | The key corresponding to the added value. <br>The value range is all integers. |
| config | [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | Yes | Configuration of the data proxy operation. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 15700015 | No permission to access the data specified by the URI. |
| [15700014](../errorcode-datashare.md#15700014-incorrect-parameters-for-shared-configuration) | The parameter format is incorrect or the value range is invalid. |
| [15700011](../errorcode-datashare.md#15700011-uri-not-exist) | The URI does not exist. |
| [15700000](../errorcode-datashare.md#15700000-internal-error) | Inner error. Possible causes: The service is not ready or is being restarted abnormally. |

