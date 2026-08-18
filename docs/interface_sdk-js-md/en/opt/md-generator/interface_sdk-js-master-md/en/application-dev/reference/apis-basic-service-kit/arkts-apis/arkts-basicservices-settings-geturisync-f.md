# getUriSync

## Modules to Import

```TypeScript
```

## getUriSync

```TypeScript
function getUriSync(name: string): string
```

Get settingsdata uri (synchronous method)

**Since:** 23

**Deprecated since:** 26.0.0

<!--Device-settings-function getUriSync(name: string): string--><!--Device-settings-function getUriSync(name: string): string-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Examples**

```TypeScript
// Obtain the URI of a data item.
let uriVar:string = settings.getUriSync(settings.display.SCREEN_BRIGHTNESS_STATUS);
```
