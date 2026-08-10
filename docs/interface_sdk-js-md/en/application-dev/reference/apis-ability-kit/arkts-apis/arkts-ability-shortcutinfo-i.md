# ShortcutInfo

快捷方式的配置信息。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface ShortcutInfo--><!--Device-unnamed-export interface ShortcutInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## appIndex

```TypeScript
appIndex: int
```

快捷方式所属应用的分身索引。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ShortcutInfo-appIndex: int--><!--Device-ShortcutInfo-appIndex: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## bundleName

```TypeScript
bundleName: string
```

快捷方式所属应用的包名。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ShortcutInfo-bundleName: string--><!--Device-ShortcutInfo-bundleName: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## hostAbility

```TypeScript
hostAbility?: string
```

快捷方式的宿主组件名, 即承载此快捷方式的组件名。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ShortcutInfo-hostAbility?: string--><!--Device-ShortcutInfo-hostAbility?: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## icon

```TypeScript
icon?: string
```

快捷方式的图标，取值为资源文件的索引。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ShortcutInfo-icon?: string--><!--Device-ShortcutInfo-icon?: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## iconId

```TypeScript
iconId?: long
```

快捷方式图标的资源ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ShortcutInfo-iconId?: long--><!--Device-ShortcutInfo-iconId?: long-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## id

```TypeScript
id: string
```

快捷方式的ID。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ShortcutInfo-id: string--><!--Device-ShortcutInfo-id: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## label

```TypeScript
label?: string
```

快捷方式的标签信息，即快捷方式对外显示的文字描述信息。可以是描述性内容，也可以是标识label的资源索引。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ShortcutInfo-label?: string--><!--Device-ShortcutInfo-label?: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## labelId

```TypeScript
labelId?: long
```

快捷方式标签信息为资源索引时的资源ID。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ShortcutInfo-labelId?: long--><!--Device-ShortcutInfo-labelId?: long-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## moduleName

```TypeScript
moduleName?: string
```

快捷方式的模块名。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ShortcutInfo-moduleName?: string--><!--Device-ShortcutInfo-moduleName?: string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## sourceType

```TypeScript
sourceType: int
```

快捷方式来源类型。0表示自定义快捷方式，1表示静态快捷方式，2表示动态快捷方式。从API version 23开始，支持动态快捷方式。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-ShortcutInfo-sourceType: int--><!--Device-ShortcutInfo-sourceType: int-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## visible

```TypeScript
visible?: boolean
```

快捷方式是否显示。true：快捷方式显示；false：快捷方式不显示。默认值为true。

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ShortcutInfo-visible?: boolean--><!--Device-ShortcutInfo-visible?: boolean-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## wants

```TypeScript
wants?: Array<ShortcutWant>
```

快捷方式内定义的目标wants信息集合。

**Type:** Array&lt;ShortcutWant&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ShortcutInfo-wants?: Array<ShortcutWant>--><!--Device-ShortcutInfo-wants?: Array<ShortcutWant>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

