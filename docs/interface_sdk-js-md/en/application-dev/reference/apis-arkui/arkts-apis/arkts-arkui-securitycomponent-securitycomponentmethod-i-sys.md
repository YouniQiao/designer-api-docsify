# SecurityComponentMethod

Declares the interface for the method of a security component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface SecurityComponentMethod--><!--Device-unnamed-export declare interface SecurityComponentMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## key

```TypeScript
key(value: string | undefined): this
```

Key. User can set an key to the component to identify it.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SecurityComponentMethod-key(value: string | undefined): this--><!--Device-SecurityComponentMethod-key(value: string | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | string \| undefined | Yes | identify the key of the component. |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityComponentMethod](arkts-arkui-securitycomponent-securitycomponentmethod-i.md) | Returns the attribute of the security component. |

