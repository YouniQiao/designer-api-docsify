# update

## update

```TypeScript
function update(handle: number, token?: Uint8Array, options: HuksOptions, callback: AsyncCallback<HuksResult>): void
```

Updates the key operation data by segment. This API uses an asynchronous callback to return the result.

The **huks.init**, **huks.update**, and **huks.finish** must be used together.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [huks.updateSession](arkts-universalkeystore-huks-updatesession-f.md#updatesession)(

<!--Device-huks-function update(handle: number, token?: Uint8Array, options: HuksOptions, callback: AsyncCallback<HuksResult>): void--><!--Device-huks-function update(handle: number, token?: Uint8Array, options: HuksOptions, callback: AsyncCallback<HuksResult>): void-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handle | number | Yes | Handle of the **update** operation, which is of the uint64 type. |
| token | Uint8Array | No | Token of the **update** operation. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Parameter set used for the **update** operation. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;HuksResult&gt; | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**, and **data** is the obtained **HuksResult**. Otherwise, **err** is an error object. |


## update

```TypeScript
function update(handle: number, token?: Uint8Array, options: HuksOptions): Promise<HuksResult>
```

Updates the key operation data by segment. This API uses a promise to return the result.

The **huks.init**, **huks.update**, and **huks.finish** must be used together.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [huks.updateSession](arkts-universalkeystore-huks-updatesession-f.md#updatesession)(handle:

<!--Device-huks-function update(handle: number, token?: Uint8Array, options: HuksOptions): Promise<HuksResult>--><!--Device-huks-function update(handle: number, token?: Uint8Array, options: HuksOptions): Promise<HuksResult>-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| handle | number | Yes | Handle of the **update** operation, which is of the uint64 type. |
| token | Uint8Array | No | Token of the **update** operation. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Parameter set used for the **update** operation. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;HuksResult&gt; | Promise that returns **HuksResult**. |

