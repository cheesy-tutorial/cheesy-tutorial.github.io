import React from 'react';
import styled from '@emotion/styled';

import NightImage from './images/night.png';
import DayImage from './images/day.png';

const StyledSwitch = styled('div')`
  display: flex;
  justify-content: flex-end;
  width: 100%;
  padding: 0 20px 0 25px;
`;

export const DarkModeSwitch = ({ isDarkThemeActive, toggleActiveTheme }) => (
  <StyledSwitch>
    <label id="switch" className="switch">
      <input
        type="checkbox"
        id="slider"
        onChange={toggleActiveTheme}
        checked={isDarkThemeActive ? false : true}
      />
      <span className="slider round"></span>
    </label>
  </StyledSwitch>
);
