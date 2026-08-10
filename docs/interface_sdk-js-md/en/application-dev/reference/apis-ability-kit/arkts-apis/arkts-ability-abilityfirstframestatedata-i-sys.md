# AbilityFirstFrameStateData (System API)

定义了首帧绘制完成事件回调上报的数据结构。通过  
[on](./../@ohos.app.ability.appManager:appManager.on(type: 'abilityFirstFrameState', observer: AbilityFirstFrameStateObserver, bundleName?: string))注册监听Ability首帧绘制完成事件后，可使用  
[AbilityFirstFrameStateObserver](arkts-ability-abilityfirstframestateobserver-i-sys.md)的  
[onAbilityFirstFrameDrawn](arkts-ability-abilityfirstframestateobserver-i-sys.md#onabilityfirstframedrawn)回调获取上报的数据结构。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface AbilityFirstFrameStateData--><!--Device-unnamed-export interface AbilityFirstFrameStateData-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## abilityName

```TypeScript
abilityName: string
```

Ability名称。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AbilityFirstFrameStateData-abilityName: string--><!--Device-AbilityFirstFrameStateData-abilityName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## appIndex

```TypeScript
appIndex: int
```

DLP沙盒的索引。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** 0

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AbilityFirstFrameStateData-appIndex: int--><!--Device-AbilityFirstFrameStateData-appIndex: int-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## bundleName

```TypeScript
bundleName: string
```

应用Bundle名称。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AbilityFirstFrameStateData-bundleName: string--><!--Device-AbilityFirstFrameStateData-bundleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## isColdStart

```TypeScript
isColdStart: boolean
```

是否冷启动。true表示冷启动，false表示热启动。

**Type:** boolean

**Default:** false

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AbilityFirstFrameStateData-isColdStart: boolean--><!--Device-AbilityFirstFrameStateData-isColdStart: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## moduleName

```TypeScript
moduleName: string
```

应用Module名称。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-AbilityFirstFrameStateData-moduleName: string--><!--Device-AbilityFirstFrameStateData-moduleName: string-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

