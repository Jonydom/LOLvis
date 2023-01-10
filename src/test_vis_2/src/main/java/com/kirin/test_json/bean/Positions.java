package com.kirin.test_json.bean;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @author Xiyao Li
 * @date 2022/12/24 01:39
 */

@Data
@AllArgsConstructor
@NoArgsConstructor
public class Positions {
    private PositionInfo jungle;

    private PositionInfo top;

    private PositionInfo support;
}
