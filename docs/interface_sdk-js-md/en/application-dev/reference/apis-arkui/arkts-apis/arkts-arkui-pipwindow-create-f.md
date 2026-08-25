# create

## Modules to Import

```TypeScript
import { PiPWindow } from 'kits/@kit.ArkUI';
```

## create

```TypeScript
function create(config: PiPConfiguration): Promise<PiPController>
```

Creates a PiP controller. This API uses a promise to return the result.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [PiPConfiguration](arkts-arkui-pipwindow-pipconfiguration-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PiPController](arkts-arkui-pipwindow-pipcontroller-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |


## create

```TypeScript
function create(config: PiPConfiguration, contentNode: typeNode.XComponent): Promise<PiPController>
```

Creates a PiP controller. This API uses **typeNode** to add a custom UI node for PiP. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [PiPConfiguration](arkts-arkui-pipwindow-pipconfiguration-i.md) | Yes |
| contentNode | typeNode.XComponent | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PiPController](arkts-arkui-pipwindow-pipcontroller-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
