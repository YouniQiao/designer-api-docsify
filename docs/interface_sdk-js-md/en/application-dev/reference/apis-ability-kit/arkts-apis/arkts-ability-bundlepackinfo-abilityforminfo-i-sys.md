# AbilityFormInfo (System API)

卡片信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface AbilityFormInfo--><!--Device-unnamed-export interface AbilityFormInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

## defaultDimension

```TypeScript
readonly defaultDimension: string
```

表示卡片默认外观规格，取值必须在supportDimensions配置的列表中。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AbilityFormInfo-readonly defaultDimension: string--><!--Device-AbilityFormInfo-readonly defaultDimension: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

## name

```TypeScript
readonly name: string
```

表示forms的名称。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AbilityFormInfo-readonly name: string--><!--Device-AbilityFormInfo-readonly name: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

## scheduledUpdateTime

```TypeScript
readonly scheduledUpdateTime: string
```

表示卡片定点刷新的时间，采用24小时计数，精确到分钟。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AbilityFormInfo-readonly scheduledUpdateTime: string--><!--Device-AbilityFormInfo-readonly scheduledUpdateTime: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

## supportDimensions

```TypeScript
readonly supportDimensions: Array<string>
```

表示卡片外观规格，取值为“1*2”，“2*2”，“2*4”，“4*4”，定义卡片时至少要指定一个卡片规格。

**Type:** Array&lt;string&gt;

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AbilityFormInfo-readonly supportDimensions: Array<string>--><!--Device-AbilityFormInfo-readonly supportDimensions: Array<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

## type

```TypeScript
readonly type: string
```

表示forms的类型。

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AbilityFormInfo-readonly type: string--><!--Device-AbilityFormInfo-readonly type: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

## updateDuration

```TypeScript
readonly updateDuration: int
```

表示卡片定时刷新的更新频率，单位：分钟，取值为30的倍数值。卡片的最高频率为每30分钟刷新一次，和定点刷新二选一，二者都配置的情况下，定时优先。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AbilityFormInfo-readonly updateDuration: int--><!--Device-AbilityFormInfo-readonly updateDuration: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

## updateEnabled

```TypeScript
readonly updateEnabled: boolean
```

表示该卡片是否支持定时刷新，true表示卡片支持定时刷新，false表示不支持。

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-AbilityFormInfo-readonly updateEnabled: boolean--><!--Device-AbilityFormInfo-readonly updateEnabled: boolean-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

