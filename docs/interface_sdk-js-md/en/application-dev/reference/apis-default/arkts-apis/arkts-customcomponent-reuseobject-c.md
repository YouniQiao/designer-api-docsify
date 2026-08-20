# ReuseObject

Define ReuseObject for aboutToReuse method.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare class ReuseObject--><!--Device-unnamed-export declare class ReuseObject-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_get

```TypeScript
$_get(key: string): RecordData
```

Get value from the ReuseObject by key.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReuseObject-$_get(key: string): RecordData--><!--Device-ReuseObject-$_get(key: string): RecordData-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | the key of target value. |

**Return value:**

| Type | Description |
| --- | --- |
| [RecordData](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-recorddata-t.md) | the target value. |

## has

```TypeScript
has(key: string): boolean
```

Returns if the key is in the ReuseObject.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReuseObject-has(key: string): boolean--><!--Device-ReuseObject-has(key: string): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | the key of target value. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | if the key is in the ReuseObject. |

## keys

```TypeScript
keys(): string[]
```

Returns the keys array of the ReuseObject.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ReuseObject-keys(): string[]--><!--Device-ReuseObject-keys(): string[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| string[] | the keys array of the ReuseObject. |

