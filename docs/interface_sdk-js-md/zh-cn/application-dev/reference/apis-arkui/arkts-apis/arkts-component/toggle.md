# component/toggle

组件提供勾选框样式、状态按钮样式和开关样式。
 > **说明：**
 >
 > - 本模块同时支持ArkTS-Dyn、ArkTS-Sta。
 > - 从API版本26.0.0开始，Toggle组件支持新材质效果。Toggle组件使用通用新材质属性systemMaterial时，不同[ToggleType](../arkts-arkui-component/toggle-toggletype-e.md)类型的效果不同：
 > >   - ToggleType.Checkbox：当前未适配系统材质效果，设置系统材质不会出现系统材质相关的动效和视觉效果。
 > >   - ToggleType.Switch：传入材质参数时，使用组件内部预设的视觉参数，传入的材质参数仅作为开启新材质的开关标记，不影响实际视觉效果。主要影响Toggle的滑块大小、滑块样式、阴影等视觉属性。设置
 > [switchPointColor](switchPointColor)后会出现点光源效果，点光源颜色跟随switchPointColor的设置。传入undefined时，新材质不生效，表现为原先的Toggle样式。
 > >   - ToggleType.Button：设置系统材质的效果与[Button](../../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-mouseevent-button-e.md)组件设置系统材质的效果相同，主要影响背景颜色、边框、阴影等视觉属性。
 ###### 子组件
 仅当ToggleType设置为Button时，可包含子组件。


## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [Toggle](toggle-toggle-f.md#toggle) | Defines Toggle Component. |

### 类

| 名称 | 说明 |
| --- | --- |
| [ExtendableToggle](toggle-extendabletoggle-c.md) | Defines the Extendable Toggle. |

### 接口

| 名称 | 说明 |
| --- | --- |
| [SwitchStyle](toggle-switchstyle-i.md) | Switch类型的样式。 |
| [ToggleAttribute](toggle-toggleattribute-i.md) | 除支持[通用属性]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_外，还支持以下属性： |
| [ToggleConfiguration](toggle-toggleconfiguration-i.md) | 开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_。 |
| [ToggleOptions](toggle-toggleoptions-i.md) | Toggle的信息。  @since版本号高于内层元素版本号的情况，但这不影响接口的使用。 |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [ToggleType](toggle-toggletype-e.md) | Toggle的样式。 |

