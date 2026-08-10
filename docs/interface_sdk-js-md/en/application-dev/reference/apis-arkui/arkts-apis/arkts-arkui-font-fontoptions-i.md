# FontOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-font-interface FontOptions--><!--Device-font-interface FontOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { font } from 'kits/@kit.ArkUI';
```

## familyName

```TypeScript
familyName: string | Resource
```

设置注册的字体名称。

**Type:** string \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FontOptions-familyName: string | Resource--><!--Device-FontOptions-familyName: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## familySrc

```TypeScript
familySrc: string | Resource
```

设置注册字体文件的路径。

**说明：**

读取系统沙箱路径内的资源时，建议使用file://路径前缀的字符串，需要确保沙箱目录路径下的文件存在并且有可读权限。

**Type:** string \| Resource

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FontOptions-familySrc: string | Resource--><!--Device-FontOptions-familySrc: string | Resource-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

