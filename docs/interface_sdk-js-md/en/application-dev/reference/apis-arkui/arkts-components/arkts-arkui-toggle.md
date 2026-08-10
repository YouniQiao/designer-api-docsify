# Toggle

组件提供勾选框样式、状态按钮样式和开关样式，适用于需要快速切换状态或进行单选确认的场景，能够有效提升交互体验与界面的直观性。

> **说明：**

> - 从API版本26.0.0开始，Toggle组件支持新材质效果。Toggle组件使用通用新材质属性[systemMaterial]{@link CommonMethod#systemMaterial}时，不同
> [ToggleType]{@link ToggleType}类型的效果不同： 
> > - ToggleType.Checkbox：当前未适配系统材质效果，设置系统材质不会出现系统材质相关的动效和视觉效果。
> > - ToggleType.Switch：传入材质参数时，使用组件内部预设的视觉参数，传入的材质参数仅作为开启新材质的开关标记，不影响实际视觉效果。主要影响Toggle的滑块大小、滑块样式、阴影等视觉属性。设置
> [switchPointColor]{@link ToggleAttribute#switchPointColor}后会出现点光源效果，点光源颜色跟随switchPointColor的设置。传入undefined时，新材质不生效，
> 表现为原先的Toggle样式。
> > - ToggleType.Button：设置系统材质的效果与[Button]{@link button}组件设置系统材质的效果相同，主要影响背景颜色、边框、阴影等视觉属性。

## 子组件

仅当ToggleType设置为Button时，可包含子组件。

## Toggle

```TypeScript
Toggle(options: ToggleOptions)
```

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ToggleInterface-(options: ToggleOptions): ToggleAttribute--><!--Device-ToggleInterface-(options: ToggleOptions): ToggleAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ToggleOptions](../arkts-apis/arkts-arkui-toggle-toggleoptions-i.md) | Yes | Toggle组件的配置选项，用于配置开关的样式类型和初始状态。 |

## Summary

- [SwitchStyle](arkts-arkui-toggle-switchstyle-i.md)
- [ToggleConfiguration](arkts-arkui-toggle-toggleconfiguration-i.md)
- [ToggleOptions](arkts-arkui-toggle-toggleoptions-i.md)
- [ToggleType](arkts-arkui-toggle-toggletype-e.md)
