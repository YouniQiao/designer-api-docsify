# InstallParam

应用包安装需指定的参数信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-bundleManager-interface InstallParam--><!--Device-bundleManager-interface InstallParam-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.MDMKit';
```

## installFlag

```TypeScript
installFlag?: number
```

安装标志。枚举值：0：应用初次安装，1：应用覆盖安装，2：应用免安装，默认值为0(应用初次安装)。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InstallParam-installFlag?: number--><!--Device-InstallParam-installFlag?: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## parameters

```TypeScript
parameters?: Record<string, string>
```

扩展参数，默认值为空。key取值支持"ohos.bms.param.enterpriseForAllUser"，若对应的value值为"true"，表示为所有用户安装应用。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt;

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InstallParam-parameters?: Record<string, string>--><!--Device-InstallParam-parameters?: Record<string, string>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## userId

```TypeScript
userId?: number
```

指示用户ID，默认值：调用方所在用户，取值范围：大于等于0。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-InstallParam-userId?: number--><!--Device-InstallParam-userId?: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

