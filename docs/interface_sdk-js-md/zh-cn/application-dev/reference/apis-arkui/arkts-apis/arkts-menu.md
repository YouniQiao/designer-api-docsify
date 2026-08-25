# menu

以垂直列表形式显示的菜单。
 > **说明：**
 >
 > - 本模块同时支持ArkTS-Dyn、ArkTS-Sta。
 > - Menu组件需和
 > bindMenu或
 > bindContextMenu
 > 方法配合使用，不支持作为普通组件单独使用。
 ###### 子组件
 包含MenuItem、MenuItemGroup子组件。
 ###### 接口
 Menu()
 作为菜单的固定容器，无参数。
 > **说明：**
 >
 > - 菜单和菜单项宽度计算规则：
 > >
 > >   - 布局过程中，期望每个菜单项的宽度一致。若子组件设置了宽度，则以constraintSize为准。
 > >
 > >   - Menu不设置宽度的情况：Menu会对子组件MenuItem、MenuItemGroup设置默认2栅格的宽度，若菜单项内容区比2栅格宽，则会自适应撑开。
 > >
 > >   - Menu设置宽度的情况：Menu会对子组件MenuItem、MenuItemGroup设置减去padding后的固定宽度。
 > >
 > >   - Menu支持设置的最小宽度为64vp。
 >
 > - Menu不支持的通用属性：外描边设置下的属性、shadow。


## 汇总

### 函数

| 名称 |
| --- |
| [Menu](arkts-arkui-menu-menu-f.md) |

### 接口

| 名称 |
| --- |
| [MenuAttribute](arkts-arkui-menu-menuattribute-i.md) |

### 枚举

| 名称 |
| --- |
| [SubMenuExpandingMode](arkts-arkui-menu-submenuexpandingmode-e.md) |
