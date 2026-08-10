# Options

Preferences实例配置选项。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-sendablePreferences-interface Options--><!--Device-sendablePreferences-interface Options-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

## Modules to Import

```TypeScript
import { sendablePreferences } from 'kits/@kit.ArkData';
```

## dataGroupId

```TypeScript
dataGroupId?: string | null
```

应用组ID，&lt;!--RP1--&gt;暂不支持指定dataGroupId在对应共享沙箱路径下创建Preferences实例。&lt;!--RP1End--&gt;

为可选参数。指定在此dataGroupId对应的沙箱路径下创建Preferences实例。当此参数不填时，默认在本应用沙箱目录下创建Preferences实例。

**模型约束：** 此属性仅在Stage模型下可用。

**Type:** string \| null

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Options-dataGroupId?: string | null--><!--Device-Options-dataGroupId?: string | null-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

## name

```TypeScript
name: string
```

Preferences实例的名称。名称长度需大于零且小于等于255字节，名称中不能包含'/'且不能以'/'结尾。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Options-name: string--><!--Device-Options-name: string-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

