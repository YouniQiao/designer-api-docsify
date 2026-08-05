# @ohos.data.dataShare

The **DataShare** module allows an application to manage its own data and share data with other applications on the same device.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace dataShare--><!--Device-unnamed-declare namespace dataShare-End-->

**System capability:** SystemCapability.DistributedDataManager.DataShare.Consumer

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createDataProxyHandle](arkts-arkdata-datashare-createdataproxyhandle-f.md#createdataproxyhandle) | Creates a **DataProxyHandle** instance. This API uses a promise to return the result. |
| [createDataShareHelper](arkts-arkdata-datashare-createdatasharehelper-f.md#createdatasharehelper) | Creates a **DataShareHelper** instance. This API uses an asynchronous callback to return the result. |
| [createDataShareHelper](arkts-arkdata-datashare-createdatasharehelper-f.md#createdatasharehelper-1) | Creates a **DataShareHelper** instance. **DataShareHelperOptions** specifies whether **DataShareHelper** is in proxy mode. This API uses an asynchronous callback to return the result. |
| [createDataShareHelper](arkts-arkdata-datashare-createdatasharehelper-f.md#createdatasharehelper-2) | Creates a **DataShareHelper** instance. **DataShareHelperOptions** specifies whether **DataShareHelper** is in proxy mode. This API uses a promise to return the result. |
| [disableSilentProxy](arkts-arkdata-datashare-disablesilentproxy-f.md#disablesilentproxy) | Disables silent access. This API uses a promise to return the result. Observe the following when using this API: - The data provider calls this API to disable silent access. - Whether silent access is disabled is determined based on the return value of this API and the **isSilentProxyEnable** field in the \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ file together. - If silent access is disabled for a URI using this API, the setting takes effect when the related **datashareHelper** API is called. Otherwise, the setting of **isSilentProxyEnable** in the **data\_\_\_ESCAPED\_UNDERSCORE\_\_\_share\_\_\_ESCAPED\_UNDERSCORE\_\_\_config.json** file is used to determine whether to disable silent access. |
| [enableSilentProxy](arkts-arkdata-datashare-enablesilentproxy-f.md#enablesilentproxy) | Enables silent access. This API uses a promise to return the result. Observe the following when using this API: - The data provider calls this API to enable silent access. - Whether silent access is enabled is determined based on the return value of this API and the **isSilentProxyEnable** field in the \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ file together. - If silent access is enabled for a URI using this API, the setting takes effect when the related **datashareHelper** API is called. Otherwise, the setting of **isSilentProxyEnable** in the **data\_\_\_ESCAPED\_UNDERSCORE\_\_\_share\_\_\_ESCAPED\_UNDERSCORE\_\_\_config.json** file is used to determine whether to enable silent access. |

### Interfaces

| Name | Description |
| --- | --- |
| [ChangeInfo](arkts-arkdata-datashare-changeinfo-i.md) | Represents the data change information, including the data change type, URI of the data changed, and changed data content. |
| [DataProxyChangeInfo](arkts-arkdata-datashare-dataproxychangeinfo-i.md) | Defines a struct for notifying subscribers of the shared configuration changes, including data change type, URI, and content. |
| [DataProxyConfig](arkts-arkdata-datashare-dataproxyconfig-i.md) | Defines a struct for the data proxy configuration. |
| [DataProxyGetResult](arkts-arkdata-datashare-dataproxygetresult-i.md) | Defines a struct for obtaining the batch operation result of shared configuration. |
| [DataProxyHandle](arkts-arkdata-datashare-dataproxyhandle-i.md) | Defines the data proxy handle, which can be used to access or manage shared configuration information. Before calling an API provided by **DataProxyHandle**, you must create a **DataProxyHandle** instance using [createDataProxyHandle]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| [DataProxyResult](arkts-arkdata-datashare-dataproxyresult-i.md) | Defines a struct for the batch operation result of shared configuration. |
| [DataShareHelper](arkts-arkdata-datashare-datasharehelper-i.md) | Provides a **DataShareHelper** instance to access or manage data on the server. Before calling an API provided by **DataShareHelper**, you must create a **DataShareHelper** instance using [createDataShareHelper]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ . |
| [DataShareHelperOptions](arkts-arkdata-datashare-datasharehelperoptions-i.md) | Represents the optional parameters of [DataShareHelper]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| [OperationResult](arkts-arkdata-datashare-operationresult-i.md) | Defines the result of the operation for subscribing to or unsubscribing from the data changes or published data. |
| [ProxyData](arkts-arkdata-datashare-proxydata-i.md) | Defines a struct for shared configurations. |
| [PublishedDataChangeNode](arkts-arkdata-datashare-publisheddatachangenode-i.md) | Defines the subscription/unsubscription result of the changes in the published data. |
| [PublishedItem](arkts-arkdata-datashare-publisheditem-i.md) | Defines the data to publish. |
| [RdbDataChangeNode](arkts-arkdata-datashare-rdbdatachangenode-i.md) | Represents the RDB data change result. The data returned by the callback is not larger than 10 MB in size. |
| [Template](arkts-arkdata-datashare-template-i.md) | Defines the struct of the template used in a subscription. |
| [TemplateId](arkts-arkdata-datashare-templateid-i.md) | Defines the **TemplateId** struct. **TemplateId** is generated by [**addTemplate**]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ to identify a template. |
| [UpdateOperation](arkts-arkdata-datashare-updateoperation-i.md) | Represents the batch update operation information. |

### Enums

| Name | Description |
| --- | --- |
| [ChangeType](arkts-arkdata-datashare-changetype-e.md) | Enumerates the data change types. |
| [DataProxyErrorCode](arkts-arkdata-datashare-dataproxyerrorcode-e.md) | Enumerates the status code returned by the batch operations of shared configuration. |
| [DataProxyMaxValueLength](arkts-arkdata-datashare-dataproxymaxvaluelength-e.md) | The maximum length of \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_, \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_, \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_2\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. |
| [DataProxyType](arkts-arkdata-datashare-dataproxytype-e.md) | Enumerates the data proxy types. |
| [SubscriptionType](arkts-arkdata-datashare-subscriptiontype-e.md) | Enumerates the data subscription types. |

