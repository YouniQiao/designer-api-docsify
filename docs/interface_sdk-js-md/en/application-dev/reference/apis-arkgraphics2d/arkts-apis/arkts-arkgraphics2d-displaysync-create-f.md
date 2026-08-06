# create

## create

```TypeScript
function create(): DisplaySync
```

Creates a **DisplaySync** object, through which you can set the frame rate of the custom UI content.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-displaySync-function create(): DisplaySync--><!--Device-displaySync-function create(): DisplaySync-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | DisplaySync** object created. |

**Example**

```TypeScript
let backDisplaySync: displaySync.DisplaySync = displaySync.create();
```

