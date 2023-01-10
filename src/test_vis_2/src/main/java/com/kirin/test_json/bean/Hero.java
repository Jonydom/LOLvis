package com.kirin.test_json.bean;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @author Xiyao Li
 * @date 2022/12/24 01:37
 */

@Data
@AllArgsConstructor
@NoArgsConstructor
public class Hero {
    private String region;
    private String tier;
    private String patch;
    private Positions positions;

    @Override
    public String toString() {
        return "Hero{" +
                "region='" + region + '\'' +
                ", tier='" + tier + '\'' +
                ", patch='" + patch + '\'' +
                ", positions=" + positions +
                '}';
    }
}
